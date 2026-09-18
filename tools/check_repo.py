#!/usr/bin/env python3
# =============================================================
# check_repo.py  —  Kannagi Diary リポジトリ検証の番人 v2
#
# commit前 / CI（GitHub Actions）で走らせ、違反があれば exit 1。
# 「検出」に徹し、自動修正はしない（判断は人間・別ツールに委ねる）。
#
# 使い方:
#   python3 tools/check_repo.py            # 全チェック
#   python3 tools/check_repo.py --quiet    # 違反のみ表示
#
# チェック項目:
#   [ENC]  UTF-8 / BOMなし / LF改行
#   [YAML] YAML妥当性（diff痕跡などの破損検出）
#   [NAME] 禁止表記・旧名・旧キーの再混入
#   [ID]   シーンカードのファイル名と scene id の一致
#   [REF]  ref: が指すファイルの実在
#
# 設計方針:
#   - registry系ファイル（旧名を"記録として"持つ）は NAME チェック除外
#   - 現行版のみ対象。archive/ と旧versionは対象外にできる
# =============================================================
import glob
import os
import re
import sys

# ---- 唯一の裁定基準（proper_noun_registry / name_change_registry と同期）----
FORBIDDEN = {
    "六ッ高校": "→ 六ッ川高校 (PN-001)",
    "飯縄": "→ 飯綱 (PN-002)",
    "藤代": "→ 香取 (name_change)",
    "アンジェリカ": "→ アンネ＝マリー (name_change)",
    "甘南備": "→ 明神 (name_change)",
}
FORBIDDEN_KEYS = {
    "omi_mizuha": "→ omiwa_mizuha (PN-003 wa脱落)",
    "angelica_fujishiro": "→ katori_anne_marie (PN-004)",
    "to_angelica": "→ to_anne_marie (PN-004)",
    "hayata": "→ izuna_shunta (フルネーム統一)",
}

# NAMEチェックを免除するファイル（旧名を"記録"として正当に含む）
NAME_CHECK_EXEMPT = [
    "production/STATE_SNAPSHOT_ch03.yaml",  # name_change_registry等を保持
    "tools/check_repo.py",
    "tools/check_canon_guard.py",
]

# 対象外にするパス（過去資産・アーカイブ・旧版）
#   方針(A): 現行版だけを厳格チェックする。過去版・OLDは検証しない。
#   旧版Configは「その版ではそう書かれていた」という履歴なので許容。
#   将来 archive/ へ隔離するのが理想だが、当面はここで除外する。
SKIP_PATHS = [
    "archive/",
    ".git/",
    "/OLD/",                       # raw/episodes/OLD/ などの旧構造
]

# 旧版Config（現行は v3.1）。ファイル名で除外する。
SKIP_FILENAMES_RE = re.compile(
    r"Config_v(?:1\.0|2\.2|2\.3|2\.4|2\.5|3\.0)\.yaml$"
)


def should_skip(path):
    if any(s in path for s in SKIP_PATHS):
        return True
    if SKIP_FILENAMES_RE.search(path):
        return True
    return False


def load_baseline():
    """既知の許容違反（EP01/EP02の未修正問題）を読み込む。
    種別|ファイル|該当 の形式。無ければ空集合。"""
    path = os.path.join(os.path.dirname(__file__), "canon_baseline.txt")
    known = set()
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                known.add(line)
    return known


def load_yaml_safe():
    try:
        import yaml
        return yaml
    except ImportError:
        return None


def main():
    quiet = "--quiet" in sys.argv
    strict = "--strict" in sys.argv   # ベースライン無視で全違反を出す
    yaml = load_yaml_safe()
    baseline = set() if strict else load_baseline()

    enc_issues, yaml_issues, name_issues, id_issues, ref_issues = [], [], [], [], []
    known_suppressed = 0

    all_yaml = [f for f in sorted(glob.glob("**/*.yaml", recursive=True)) if not should_skip(f)]
    basenames = {os.path.basename(f) for f in all_yaml}

    for f in all_yaml:
        data = open(f, "rb").read()

        # [ENC] BOM
        if data.startswith(b"\xef\xbb\xbf"):
            enc_issues.append(f"{f}: UTF-8 BOM あり")
        # [ENC] UTF-8
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            enc_issues.append(f"{f}: UTF-8 でない（要正規化）")
            continue
        # [ENC] CRLF
        if b"\r" in data:
            enc_issues.append(f"{f}: CRLF改行あり（LFへ）")

        # [YAML] 妥当性
        doc = None
        if yaml:
            try:
                doc = yaml.safe_load(text)
            except Exception as e:
                first = str(e).splitlines()[0] if str(e) else "parse error"
                yaml_issues.append(f"{f}: YAMLエラー（{first}）")

        # [NAME] 禁止表記・旧キー（ベースライン照合）
        if f not in NAME_CHECK_EXEMPT:
            for i, line in enumerate(text.splitlines(), 1):
                for term, fix in FORBIDDEN.items():
                    if term in line:
                        if f"NAME|{f}|{term}" in baseline:
                            known_suppressed += 1
                        else:
                            name_issues.append(f"{f}:{i}: 禁止表記[{term}] {fix}")
                stripped = line.strip()
                for kold, kfix in FORBIDDEN_KEYS.items():
                    if stripped.startswith(kold + ":") or stripped.startswith(kold + " :"):
                        if f"NAME|{f}|{kold}" in baseline:
                            known_suppressed += 1
                        else:
                            name_issues.append(f"{f}:{i}: 旧キー[{kold}] {kfix}")

        # [ID] シーンカードのファイル名 == scene id（ベースライン照合）
        if "scene_cards/" in f and isinstance(doc, dict):
            sc = doc.get("scene", doc)
            fid = None
            if isinstance(sc, dict):
                fid = sc.get("id") or sc.get("scene_id")
            if not fid:
                fid = doc.get("scene_id")
            fname = os.path.basename(f).replace(".yaml", "")
            if fid and fid != fname:
                if f"ID|{f}|{fid}" in baseline:
                    known_suppressed += 1
                else:
                    id_issues.append(f"{f}: ファイル名≠id（id={fid}）")

        # [REF] ref: の参照先実在（.yamlを指すもののみ）
        for i, line in enumerate(text.splitlines(), 1):
            for m in re.finditer(r'ref:\s*["\']?[^"\'#\n]*?([A-Za-z_0-9]+\.yaml)', line):
                target = m.group(1)
                if target not in basenames:
                    ref_issues.append(f"{f}:{i}: ref先が見つからない[{target}]")

    # ---- レポート ----
    groups = [
        ("ENC  エンコーディング", enc_issues),
        ("YAML 妥当性", yaml_issues),
        ("NAME 表記・旧名", name_issues),
        ("ID   ファイル名とid", id_issues),
        ("REF  参照解決", ref_issues),
    ]
    total = sum(len(g[1]) for g in groups)

    suffix = f"（既知 {known_suppressed}件は許容）" if known_suppressed and not strict else ""
    if total == 0:
        print(f"✅ 全チェック通過（YAML {len(all_yaml)}件）{suffix}")
        return 0

    print(f"❌ 新規違反 {total}件（YAML {len(all_yaml)}件中）{suffix}\n")
    for label, issues in groups:
        if issues:
            print(f"── [{label}] {len(issues)}件")
            for v in issues:
                print(f"   {v}")
            print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
