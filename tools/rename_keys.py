#!/usr/bin/env python3
# =============================================================
# rename_keys.py
# YAMLキーの改名（構造変更 / GP-003: 承認済み前提で実行）
#
# 対象:
#   [addressing_rules.yaml]
#     omi_mizuha        -> omiwa_mizuha        (誤記: wa脱落)
#     angelica_fujishiro-> katori_anne_marie   (改名)
#     to_angelica       -> to_anne_marie       (改名: 名前ベース原則)
#   [Config_v2.5.yaml]  CHARACTER_LAYER をフルネームキーへ統一
#     hayata    -> izuna_shunta
#     mizuha    -> omiwa_mizuha
#     mayo      -> hikawa_mao
#     sumiyoshi -> sumiyoshi_shotaro
#     myojin    -> myojin_akira
#     （定義キー・relationships参照キーの両方）
#
# 方式:
#   行頭インデント＋'key:' の形で現れるYAMLキーのみを置換する。
#   値の中の同名文字列は触らない（キーとしての出現に限定）。
#   コメント・書式は保持。
#
# 使い方:
#   python3 rename_keys.py --dry-run
#   python3 rename_keys.py --apply
# =============================================================
import argparse
import re
import sys

# ファイル名 -> [(old_key, new_key), ...]
# 注: ファイル名はリポジトリ実体に合わせて調整可能
RENAMES = {
    "addressing_rules.yaml": [
        ("omi_mizuha", "omiwa_mizuha"),
        ("angelica_fujishiro", "katori_anne_marie"),
        ("to_angelica", "to_anne_marie"),
    ],
    "Config_v2.5.yaml": [
        ("hayata", "izuna_shunta"),
        ("mizuha", "omiwa_mizuha"),
        ("mayo", "hikawa_mao"),
        ("sumiyoshi", "sumiyoshi_shotaro"),
        ("myojin", "myojin_akira"),
    ],
}


def rename_keys_in_text(text, pairs):
    """行頭インデント + key: の形のキーだけ置換する。"""
    changes = []
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        new_line = line
        for old, new in pairs:
            # ^(空白)old(空白可): の形。値部分は保持。
            pat = re.compile(r"^(\s*)" + re.escape(old) + r"(\s*):")
            if pat.search(new_line):
                new_line = pat.sub(r"\1" + new + r"\2:", new_line)
                changes.append((old, new))
        out.append(new_line)
    return "".join(out), changes


def match_file(path):
    """パス末尾でファイルを同定（接頭辞ID・v2_5/v2.5の揺れを吸収）。"""
    base = path.replace("\\", "/").split("/")[-1]
    # 比較用に正規化: ドット/アンダースコアを除いた小文字
    def norm(s):
        return s.lower().replace(".", "").replace("_", "")
    nbase = norm(base)
    for canonical in RENAMES:
        if norm(canonical) in nbase:
            return canonical
    return None


def main():
    import glob
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--glob", default="**/*.yaml")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run

    paths = sorted(glob.glob(args.glob, recursive=True))
    total = 0
    for path in paths:
        canonical = match_file(path)
        if not canonical:
            continue
        pairs = RENAMES[canonical]
        text = open(path, encoding="utf-8").read()
        new_text, changes = rename_keys_in_text(text, pairs)
        if new_text != text:
            total += 1
            from collections import Counter
            c = Counter(changes)
            print(f"[RENAME] {path}  (-> {canonical})")
            for (old, new), n in c.items():
                print(f"    {old} -> {new}  ×{n}")
            if apply:
                open(path, "w", encoding="utf-8", newline="\n").write(new_text)

    mode = "適用済み" if apply else "ドライラン（未適用）"
    print(f"\n== {mode}: {total} ファイル ==")
    if not apply and total:
        print("   問題なければ --apply（gitブランチ上）")


if __name__ == "__main__":
    main()
