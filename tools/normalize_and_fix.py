#!/usr/bin/env python3
# =============================================================
# normalize_and_fix.py
# かんなぎダイアリー リポジトリ一括修正スクリプト
#
# 役割（2層）:
#   STAGE 1: 全YAMLを UTF-8 (LF, BOMなし) へ正規化する
#   STAGE 2: 表示値の旧表記→新表記を安全に置換する
#
# 設計方針:
#   - proper_noun_registry / name_change_registry を唯一の裁定基準とする
#   - 「表示値の置換」のみ自動適用（プロ―ズ出力に直結）
#   - 「YAMLキーの改名」は構造変更（GP-003: 承認必須）なので
#     このスクリプトでは行わない。別途 rename_keys.py で対話的に実施。
#   - 置換は順序依存に注意（部分文字列事故の回避）
#
# 使い方:
#   1) リポジトリのルートで実行
#   2) まず --dry-run で差分を確認
#   3) 問題なければ --apply（git管理下のブランチ上で）
#
#   python3 normalize_and_fix.py --dry-run
#   python3 normalize_and_fix.py --apply
# =============================================================

import argparse
import glob
import os
import sys

# ---- 置換ルール（唯一の裁定基準と同期させること）-------------
# (old, new, note)。順序が重要：長い/限定的なものを先に。
DISPLAY_REPLACEMENTS = [
    # 学校名：必ず「六ッ高校」を先に処理（六ッ川高校への二重化を防ぐ）
    ("六ッ高校", "六ッ川高校", "PN-001 川脱落の誤記"),
    # 主人公表記：縄→綱
    ("飯縄", "飯綱", "PN-002 旧表記（縄）"),
    # 命名変更：藤代→香取（苗字）、アンジェリカ→アンネ＝マリー（名前）
    ("藤代", "香取", "name_change 旧苗字"),
    ("アンジェリカ", "アンネ＝マリー", "name_change 旧名"),
    # 第一章本文用（YAMLには通常無いが保険）：甘南備→明神
    ("甘南備", "明神", "name_change 旧名（本文側）"),
]

# ---- 自動置換してはいけない要注意語（検出のみ）---------------
# 「六ッ高」単独（六ッ高校でない）は文脈依存のため手動判断
FLAG_ONLY = [
    ("六ッ高", "六ッ高校 か むつこう か文脈判断が必要。六ッ高校処理後の残存を確認"),
]

# ---- YAMLキー改名（構造変更：このスクリプトでは触れない）-----
STRUCTURAL_KEYS_DO_NOT_AUTO = [
    ("hayata", "izuna_shunta", "Config_v2.5 主人公キー。参照箇所多数"),
    ("angelica_fujishiro", "katori_anne_marie", "addressing_rules アクターキー"),
    ("to_angelica", "to_katori", "addressing_rules 全アクターの参照キー"),
]


def detect_encoding(path):
    data = open(path, "rb").read()
    for enc in ("utf-8-sig", "utf-8", "shift_jis", "cp932", "euc-jp"):
        try:
            data.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    return None


def process(paths, apply):
    changed_files = 0
    for path in paths:
        enc = detect_encoding(path)
        if enc is None:
            print(f"[SKIP] {path}: エンコーディング判定不可")
            continue
        raw = open(path, "rb").read()
        text = raw.decode(enc)
        orig = text

        # STAGE 1: 改行をLFへ、BOM除去（decodeで対応済み）
        normalized_newlines = text.replace("\r\n", "\n").replace("\r", "\n")
        text = normalized_newlines

        # STAGE 2: 表示値置換
        per_file_changes = []
        for old, new, note in DISPLAY_REPLACEMENTS:
            if old in text:
                cnt = text.count(old)
                text = text.replace(old, new)
                per_file_changes.append(f"    置換 {old}→{new} ×{cnt}  ({note})")

        # FLAG: 要注意語の残存検出
        flags = []
        for term, note in FLAG_ONLY:
            if term in text:
                flags.append(f"    ⚠ 残存 [{term}] ×{text.count(term)}  ({note})")

        enc_change = (enc != "utf-8")
        will_change = (text != orig) or enc_change

        if will_change:
            changed_files += 1
            print(f"[FIX] {os.path.basename(path)}")
            if enc_change:
                print(f"    エンコーディング {enc} → utf-8 (LF)")
            for c in per_file_changes:
                print(c)
            for fl in flags:
                print(fl)
            if apply:
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
        else:
            # 変更なしでもフラグだけは出す
            if flags:
                print(f"[FLAG] {os.path.basename(path)}")
                for fl in flags:
                    print(fl)

    print()
    mode = "適用済み" if apply else "ドライラン（未適用）"
    print(f"== {mode}: {changed_files} ファイルが対象 ==")
    if not apply and changed_files:
        print("   問題なければ --apply を付けて実行してください（gitブランチ上推奨）")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="実際に書き換える")
    ap.add_argument("--dry-run", action="store_true", help="差分のみ表示")
    ap.add_argument("--glob", default="**/*.yaml", help="対象グロブ")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run

    paths = sorted(glob.glob(args.glob, recursive=True))
    if not paths:
        print(f"対象ファイルなし: {args.glob}")
        sys.exit(1)

    print(f"対象: {len(paths)} ファイル\n")
    process(paths, apply)

    # 構造変更の注意喚起
    print()
    print("---- 注意: YAMLキー改名は未実施（構造変更 / 承認必須）----")
    for old, new, note in STRUCTURAL_KEYS_DO_NOT_AUTO:
        print(f"    {old} → {new}  ({note})")
    print("    → rename_keys.py で対話的に実施するか、手動で。")


if __name__ == "__main__":
    main()
