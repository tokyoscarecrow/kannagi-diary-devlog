# Current Project State

## Overview

This document defines the **current authoritative state** of the project.

It provides a quick reference for:
- Which configs are active
- What structure is currently being worked on
- What the project is focusing on at this stage

If you are new to the repository, start here.

> Last updated: 2026-07-18
> For change history, see `raw/decision_logs/CHANGELOG.md`

---

## Layer Architecture (L0–L5)

The system is organized into six layers. Each layer constrains the one below it.

| Layer | File | Role |
|---|---|---|
| L0 | `raw/Config/GLOBAL_CONFIG.yaml` | Governance. How the system must behave |
| L1 | `raw/Config/PROJECT_MASTER_CONTEXT.yaml` | Theme principles. What the project is |
| L2 | `raw/Config/WORLD_AND_RULE_CONFIG.yaml` | World laws. Magic system, social rules |
| L3 | `raw/episodes/ep03_structure.yaml` | Episode structure and progression |
| L4 | `raw/scene_cards/EP03/*.yaml` | Scene cards (schema: `SCENE_CARD_TEMPLATE.v1.1.yaml`) |
| L5 | — | Prose generation output |

L0 is enforced across all lower layers. Where any conflict arises, L0 prevails.

---

## Active Core Configs (Authoritative)

### Top-Level (Non-negotiable)

- `raw/Config/GLOBAL_CONFIG.yaml` (L0, v0.1.0)
- `raw/Config/PROJECT_MASTER_CONTEXT.yaml` (L1, v1.0.0)

These define:
- What the project is
- How the system must behave

---

### World Law Layer

- `raw/Config/WORLD_AND_RULE_CONFIG.yaml` (L2, v1.0.0)

This defines the origin and principles of magic, ability structure, and social
rules. It is **not a reference to fill gaps with — it is a specification to
validate generated output against.**

---

### Domain Configs (Active)

- `raw/Config/Config_v3.1.yaml` — **current authoritative domain config**
- `raw/Config/addressing_rules.yaml` (v1.0)

These define:
- Character behavior and speech style
- Generation constraints
- Interaction and addressing consistency

> Note: `Config_v3.0.yaml` remains in the repository as the immediately
> preceding version. Versions v1.0–v2.5 are retained as history.

---

### Structure Definition

- `raw/episodes/ep03_structure.yaml` (v1.0) — **current**
- `raw/episodes/ep02_structure.yaml` — reference (structure complete)

These define:
- Scene structure (SC)
- Narrative progression
- Tension design

---

### Scene Card Schema

- `templates/SCENE_CARD_TEMPLATE.v1.1.yaml` (v1.1.0)

All scene cards from EP03 onward conform to this schema.

---

## Current Episode Focus

### EP03 — Act II, First Half (Active Development)

The project is currently focused on:

> **Structural design and execution of Episode 03**

Key structural conditions:

- **10 scenes (SC01–SC10)** across multiple locations
- **Dual-line alternating progression** (SC04–SC07), converging at SC07
- **Cliffhanger enforcement** — every scene ends on a hook
- **Non-converging tension curve** — the chapter ends suspended, still rising
- **Separation of witnessing from participating** — the protagonist may only
  witness the climax; participation is deferred to EP04

Defined so far: `EP03_SC01` (Open Campus), `EP03_SC02` (True North),
`EP03_SC03` (Encounter with the Antagonist)

### EP01 / EP02 — Structure Complete

EP02 (structural trap design: misdirection, perception control, explicitly
defined narrative "lies") is complete and retained as a reference case.

---

## Key Design Concepts (Current Stage)

### 1. Narrative as Structure

Narrative is treated as a sequence of constrained units (SC), not as free-form
writing.

---

### 2. Explicit Structure Governance

Scene structure is strictly controlled.

- SC count, order, and role are fixed
- Any modification requires explicit approval

---

### 3. Anti-Drift System

To prevent degradation over long sessions:

- GLOBAL_CONFIG enforces behavior
- PROJECT_MASTER_CONTEXT anchors invariants
- WORLD_AND_RULE_CONFIG validates world-law deviation
- Conflicts must be reported, not silently resolved

---

### 4. Validation over Reference

Upper layers are not consulted to fill in gaps. They are used to detect
deviation. This distinction is what makes the system auditable.

---

## Conventions

- **Encoding:** UTF-8, LF, no BOM. Shift_JIS is prohibited.
- **Change history:** `raw/decision_logs/CHANGELOG.md`
- **Design decisions:** `raw/decision_logs/`
- **Archive:** `archive/` and `raw/episodes/OLD/` retain superseded versions
  and are intentionally left unmodified.

---

## Current Constraints

- Structure cannot be modified without approval
- AI operates only within defined constraints
- All generation must respect Config hierarchy

---

## Status Summary

- Multi-layer config system: **Active (L0–L5)**
- GLOBAL_CONFIG: **Active**
- PROJECT_MASTER_CONTEXT: **Active**
- WORLD_AND_RULE_CONFIG: **Active**
- Domain config: **v3.1**
- EP01 / EP02 structure: **Complete**
- EP03 structure: **Defined — SC01–SC03 authored, SC04–SC10 pending**
- Governance rules: **In operation**
- Encoding normalization: **Complete (repository-wide UTF-8)**

---

## Known Issues

- **`raw/scene_cards/EP01/EP01_SC08.yaml` fails YAML parsing.**
  An unapplied diff remains pasted inside the file (lines 36–37, 42–43, 71,
  74–77): stray `+` markers, invalid `- description:` list items under a
  mapping, and full-width spaces. The `+` lines appear to be the intended
  revision, but resolving this requires a narrative design decision.
  All other 32 YAML files parse cleanly.
- EP02 scene cards use three mixed wrapper formats, unresolved:
  - `scene:[]` — SC01, SC02
  - `scenes:[]` — SC03
  - flat — SC04–SC10
  - `SCENE_CARD_TEMPLATE.v1.1.yaml` standardizes on flat. Only SC01–SC03 remain
    to be migrated.
- `raw/Config/README.md` documents per-version notes only up to v2.5.
  Entries for v3.0 and v3.1 are not yet written.

---

## Next Direction

- Authoring EP03 SC04–SC10
- Stabilizing long-form narrative generation
- Expanding structural design patterns
- Testing governance under complex scenarios

---

## Notes

This document represents the **current state**, not the full history.

For historical changes:
- See `raw/decision_logs/CHANGELOG.md`
- See `archive/`
- See versioned config files

---

---

# 現在のプロジェクト状態（日本語版）

## 概要

本ドキュメントは、プロジェクトの**現在の正本状態**を示す。

以下を素早く把握するための参照である：

- 現在有効なConfig
- 進行中の構造
- 現段階の焦点

初めてこのリポジトリを閲覧する場合は、本ファイルから読むことを推奨する。

> 最終更新：2026-07-18
> 変更履歴は `raw/decision_logs/CHANGELOG.md` を参照

---

## レイヤー構成（L0〜L5）

本システムは6層で構成される。各層は下位層を拘束する。

| 層 | ファイル | 役割 |
|---|---|---|
| L0 | `raw/Config/GLOBAL_CONFIG.yaml` | 統治。システムの振る舞いの規律 |
| L1 | `raw/Config/PROJECT_MASTER_CONTEXT.yaml` | テーマ原理。作品の定義 |
| L2 | `raw/Config/WORLD_AND_RULE_CONFIG.yaml` | 世界法則。魔法体系・社会規則 |
| L3 | `raw/episodes/ep03_structure.yaml` | エピソード構造・進行設計 |
| L4 | `raw/scene_cards/EP03/*.yaml` | シーンカード（スキーマ：`SCENE_CARD_TEMPLATE.v1.1.yaml`） |
| L5 | — | 本文生成 |

L0は全下位層に効く。矛盾が生じた場合はL0を正とする。

---

## 有効なコアConfig（正本）

### 最上位（不変）

- `raw/Config/GLOBAL_CONFIG.yaml`（L0 / v0.1.0）
- `raw/Config/PROJECT_MASTER_CONTEXT.yaml`（L1 / v1.0.0）

これらは：

- プロジェクトの定義
- 生成ルールの規律

を決定する。

---

### 世界法則レイヤー

- `raw/Config/WORLD_AND_RULE_CONFIG.yaml`（L2 / v1.0.0）

魔法の起源・原理・能力構成・社会規則を定義する。

本ファイルは「**参照して補う**」ものではなく、「**逸脱していないかを検証する**」
ためのものである。

---

### ドメインConfig（有効）

- `raw/Config/Config_v3.1.yaml` — **現行の正本**
- `raw/Config/addressing_rules.yaml`（v1.0）

これらは：

- キャラクター挙動・口調
- 生成制約
- 会話・呼称の一貫性

を定義する。

> 補足：`Config_v3.0.yaml` は直前版としてリポジトリに残置。
> v1.0〜v2.5 は履歴として保持する。

---

### 構造定義

- `raw/episodes/ep03_structure.yaml`（v1.0）— **現行**
- `raw/episodes/ep02_structure.yaml` — 参照（構造確定済）

これにより：

- シーン構造（SC）
- 進行設計
- テンション設計

が規定される。

---

### シーンカード・スキーマ

- `templates/SCENE_CARD_TEMPLATE.v1.1.yaml`（v1.1.0）

EP03以降の全シーンカードは本スキーマに準拠する。

---

## 現在のエピソード焦点

### EP03（第二幕・前半／開発中）

現在の主目的は：

> **Episode 03 における構造設計と実行**

主な構造条件：

- **複数舞台・全10話構成**（SC01〜SC10）
- **2ライン交互進行**（SC04〜SC07）と、SC07での収束
- **全SCラストのクリフハンガー義務化**
- **緊張曲線を収束させない**（上昇したまま章を閉じる）
- **「目撃」と「加担」の分離** — 主人公はクライマックスを目撃するのみ。
  加担はEP04へ繰り越す

定義済：`EP03_SC01`（オープンキャンパス）／`EP03_SC02`（True North）／
`EP03_SC03`（主敵との邂逅）

### EP01／EP02（構造確定）

EP02（誤誘導・認知操作・「嘘」の構造化）は完了し、参照事例として保持する。

---

## 現在の設計思想

### 1. ナラティブ＝構造

物語は、制約された単位（SC）の連鎖として扱う。

---

### 2. 構造ガバナンス

シーン構造は厳密に管理される：

- SC数・順序・役割は固定
- 変更には明示的承認が必要

---

### 3. ドリフト防止

長期生成における劣化対策：

- GLOBAL_CONFIGによる制御
- PROJECT_MASTER_CONTEXTによる固定
- WORLD_AND_RULE_CONFIGによる世界法則の逸脱検証
- 矛盾は報告する（黙って修正しない）

---

### 4. 参照ではなく検証

上位層は「不足を補うために読む」ものではなく、「逸脱を検出するために使う」。
この区別が、本システムを監査可能にしている。

---

## 規約

- **文字コード**：UTF-8 / LF / BOMなし。Shift_JIS は禁止
- **変更履歴**：`raw/decision_logs/CHANGELOG.md`
- **設計判断の記録**：`raw/decision_logs/`
- **アーカイブ**：`archive/` および `raw/episodes/OLD/` は旧版を保持する領域で、
  意図的に未改変のまま残す

---

## 現在の制約

- 構造変更は禁止（承認なし）
- AIは制約内でのみ動作
- すべての生成はConfig階層に従う

---

## 状態まとめ

- 多層Config構造：**運用中（L0〜L5）**
- GLOBAL_CONFIG：**稼働中**
- PROJECT_MASTER_CONTEXT：**稼働中**
- WORLD_AND_RULE_CONFIG：**稼働中**
- ドメインConfig：**v3.1**
- EP01／EP02構造：**確定**
- EP03構造：**定義済 — SC01〜SC03 作成済、SC04〜SC10 未着手**
- ガバナンス：**運用中**
- 文字コード正規化：**完了（リポジトリ全体UTF-8）**

---

## 既知の課題

- **`raw/scene_cards/EP01/EP01_SC08.yaml` がYAML構文エラー**
  適用されなかった差分がファイル内に残存（L36–37, L42–43, L71, L74–77）。
  行頭 `+` マーカー、マッピング配下の不正な `- description:`、全角スペース混入。
  `+` 行が採用予定の改訂内容と見られるが、本文設計上の判断を伴うため未修正。
  他32件のYAMLは正常にパースできる。
- EP02シーンカードのラップ形式が3種混在（未解消）
  - `scene:[]` — SC01, SC02
  - `scenes:[]` — SC03
  - flat — SC04〜SC10
  - `SCENE_CARD_TEMPLATE.v1.1.yaml` はflatに統一。残る移行対象はSC01〜SC03のみ
- `raw/Config/README.md` の版別解説は v2.5 まで。v3.0／v3.1 の項目が未記載

---

## 今後の方向

- EP03 SC04〜SC10 の作成
- 長編生成の安定化
- 構造設計の拡張
- ガバナンスの実証

---

## 注記

本ドキュメントは**現時点の状態**を示すものであり、履歴ではない。

履歴は以下を参照：

- `raw/decision_logs/CHANGELOG.md`
- `archive/`
- 各Configのバージョン履歴
