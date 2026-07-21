#!/usr/bin/env python3
# =============================================================
# check_canon_guard.py
# 禁止表記・旧名・非UTF8 を検出したら exit 1 で落とす番人。
# CI（GitHub Actions）に組み込めば、旧表記の再混入を防げる。
#
# 使い方:
#   python3 check_canon_guard.py
#   （リポジトリルートで実行。違反があれば非0で終了）
# =============================================================
import glob
import sys

# 唯一の裁定基準（registryと同期させること）
FORBIDDEN = {
    "六ッ高校": "→ 六ッ川高校 (PN-001)",
    "飯縄": "→ 飯綱 (PN-002)",
    "藤代": "→ 香取 (name_change)",
    "アンジェリカ": "→ アンネ＝マリー (name_change)",
    "甘南備": "→ 明神 (name_change)",
}

# 旧YAMLキー（キー位置での出現を禁止）
FORBIDDEN_KEYS = {
    "omi_mizuha": "→ omiwa_mizuha (PN-003 wa脱落)",
    "angelica_fujishiro": "→ katori_anne_marie (PN-004)",
    "to_angelica": "→ to_anne_marie (PN-004)",
    "hayata": "→ izuna_shunta (フルネーム統一)",
}

def main():
    violations = []
    enc_violations = []
    for f in sorted(glob.glob("**/*.yaml", recursive=True)):
        data = open(f, "rb").read()
        # 1) UTF-8（BOMなし）か
        if data.startswith(b"\xef\xbb\xbf"):
            enc_violations.append(f"{f}: UTF-8 BOM あり（除去せよ）")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            enc_violations.append(f"{f}: UTF-8 でない（要正規化）")
            continue
        # 2) 禁止表記
        for i, line in enumerate(text.splitlines(), 1):
            for term, fix in FORBIDDEN.items():
                if term in line:
                    violations.append(f"{f}:{i}: 禁止表記[{term}] {fix}")
            # 3) 旧キー（行頭インデント + key: の形のみ）
            stripped = line.strip()
            for kold, kfix in FORBIDDEN_KEYS.items():
                if stripped.startswith(kold + ":") or stripped.startswith(kold + " :"):
                    violations.append(f"{f}:{i}: 旧キー[{kold}] {kfix}")

    if enc_violations or violations:
        print("❌ canon guard 違反:")
        for v in enc_violations + violations:
            print(f"  {v}")
        sys.exit(1)
    print("✅ canon guard: 違反なし")

if __name__ == "__main__":
    main()
