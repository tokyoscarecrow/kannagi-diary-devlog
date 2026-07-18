# CHANGELOG

> 本ファイルは Config およびナラティブ構造の変更履歴を記録する。
> 記録単位は Config バージョン。Config 版を伴わない構造変更（EP構造・
> テンプレート・レイヤー新設）は、直近の Config 版のエントリ内に併記する。
>
> Encoding: UTF-8 (LF, BOMなし) ※Shift_JIS 禁止

---

## [3.1] - 2026-06-22 ／ 第二幕（EP03）始動

**現在の正本 Config。** 以下すべてを含む状態を「現行」とする。

### 🔄 Changed

#### 1. Config v3.1（レイヤー帰属の是正）

- `HUMAN_BEHAVIOR_CONSTRAINTS` から「1シーンに最低1つのズレを含める」を削除
  - 理由：ズレの配置は恒常制約ではなく、シーン個別の演出判断である
  - 恒常制約レイヤーに演出判断が混入していた誤帰属を是正
- `world_texture` を新設
  - 謎・ズレは基本的に置かない
  - 演出上必要な場合はシーンカード側で個別に指示する

### ➕ Added

#### 2. WORLD_AND_RULE_CONFIG v1.0.0（L2レイヤー新設）

- 世界法則（魔法の起源・原理・能力構成・社会規則）を独立ファイル化
- L1 PROJECT_MASTER_CONTEXT のテーマ原理を「動作するルール」へ落とし込む層
- 収録：`origin` / `fundamental_rules` / `ability_structure` /
  `confirmed_abilities` / `social_rules` / `erasure_method` / `legacy_reconciliation`
- 位置づけ：**参照して補うファイルではなく、逸脱していないかを検証するファイル**
- 母体：MAGIC_SYSTEM.yaml v1.0.0

#### 3. ep03_structure.yaml v1.0（第二幕・前半の構造定義）

- 全10話（SC01〜SC10）構成を確定
- `progression_structure` を新設
  - 全SCラストをクリフハンガーで終える方針を明文化
  - SC04〜SC07 の2ライン交互進行（みずは×真魚／明神×隼太）
  - SC07 で収束：「探す者たちの物語」→「探される隼太の物語」
  - 緊張曲線は収束させず、上昇したまま章を閉じる（EP02の山型と対比）
- `episode_premises` を新設（章全体に効かせる背景前提）
  - PREM-01：隼太・みずはは高校2年の受験生。正統館大学は未合格の志望校
  - PREM-02：True North の災害実績は遠隔地・抽象的にのみ語る
    （SC10 の不意打ちを保つため、地元・水害・高齢者救援を予告しない）
- `hazard_progression` / `rescue_constraints` / `foreshadow_seeds` を定義
- 「目撃」と「加担」の分離を構造条件として固定（EP03の隼太は目撃のみ）

#### 4. SCENE_CARD_TEMPLATE v1.1.0（L4標準スキーマ）

- EP02で混在した3つのラップ形式（`scene:[]` / `scenes:[]` / flat）を **flat単一** に統一
- v1.1.0 追加要素（既存フィールドは不変・後方互換）
  - `cliffhanger`（必須）：各SCのラストの引き
  - `tension` を `score_start` / `score_end` に拡張（話内変動の表現）
  - `reincarnation_seeds`（任意）：周回の種。通常の foreshadowing と区別
  - `dual_line`（任意）：2ライン交互進行のライン標識
- Encoding 規約を明記：UTF-8 (LF, BOMなし)、Shift_JIS 禁止

#### 5. EP03 シーンカード（3件）

- `EP03_SC01` オープンキャンパス
- `EP03_SC02` True North
- `EP03_SC03` 主敵との邂逅

### 🔧 Fixed

- `GLOBAL_CONFIG.yaml` / `PROJECT_MASTER_CONTEXT.yaml` を CP932 → UTF-8 (LF) へ変換
  - 最上位2レイヤー（L0/L1）が Shift_JIS のままで、GitHub 上で文字化けし、
    UTF-8前提のツールから読み取り不能だったため
  - SCENE_CARD_TEMPLATE v1.1.0 が定める Encoding 規約との矛盾を解消

### ⚠️ Known Issues

- 以下は依然として CP932。UTF-8化は未実施：
  - `docs/00_current_state.md` / `docs/02_governance.md` / `docs/60_ep02_design_notes.md`
  - `raw/scene_cards/EP02/EP02_SC05.yaml` 〜 `EP02_SC10.yaml`（6件）
- `ep03_structure.yaml` の `depends_on` は `Config@3.0` を指す。正本は v3.1 のため、
  次回更新時に `Config@3.1` へ追従させる
- `docs/00_current_state.md` の記載が実体と不一致
  - 有効ドメインConfigを `config_v2.5.yaml` と記載（実体は v3.1）
  - ファイル名の大小文字も不一致（実体は `Config_v2.5.yaml`）

---

## [3.0] - 2026-06-22

### 🔄 Major Update

#### 1. 第二幕（EP03〜）に向けた大規模更新

- `MAGOSHA_COMMON_RULES` の transformation（陰陽転換）を **廃止**
- L2 `WORLD_AND_RULE_CONFIG` の新設に伴い、世界法則を同ファイルへ移管
  - Config 本体は「キャラクター挙動・生成制約」に責務を絞る

#### 2. 新キャラクター追加

- 諏訪公命（主敵）
- 香取アンネ＝マリー
- 高島是則（故人）
- 政府コンビ

#### 3. 既存キャラクターの深化

- 隼太：トラウマ・思想・能力を再定義
- 真魚：`magic_user: false` + latent（潜在）構造へ変更

### 🧠 Structural Impact

- 世界法則と生成制約のレイヤー分離が完成し、L0〜L4 の責務境界が明確化
- 詳細設定は各設計ドキュメント（MAGIC_SYSTEM / ANTAGONIST_FACTION 等）へ外出し

### ⚠️ Breaking Changes

- transformation（陰陽転換）を前提とした既存記述は無効
- 世界法則の参照先が Config 本体から `WORLD_AND_RULE_CONFIG` へ移動

---

## [2.5] - 2026-03-23

### ➕ Added

#### 1. speech_style を CHARACTER_LAYER に追加

- キャラクターごとの発話ルールを明文化
- セリフ生成時のブレ防止のための制約を追加
- キャラクター相互の呼称を定義

### 🔄 Changed

- 飯綱隼太の口調を neutral 寄りに修正（住吉との差別化）

---

## [2.4] - 2026-02-16

### 🔄 Major Update

#### 1. CHARACTER_LAYER v1.0（破壊的変更）

- 氷川真魚の動機構造を全面更新
  - 旧：魔法者への復讐・否定
  - 新：父救出を目的とする救済志向
- 父の罪を認識した上で救出を選択する設定へ変更
- 制度に対する立場を二段階構造に再定義
  - 初期：制度破壊志向
  - 長期：制度再定義へ移行（隼太の行動が契機）
- EP02内の関係遷移を明文化
  - 隼太＝利用対象 → 希望の媒介者
- 長期的関係を「対等」へ固定
- 真魚の言語仕様を明文化（常時敬語・距離感維持）

#### 2. 明神の立場強化

- 魔法抑止側であることを明確化
- 「見殺しにしない」「人命優先」の倫理基準を追加

---

### ➕ Added

#### 3. HUMAN_BEHAVIOR_CONSTRAINTS v1.1

- 魔法使用の心理的・社会的コストを明文化
  - 魔法使用は孤立を加速し得る
  - 「使わない」選択が倫理的成立を持つ

#### 4. Episode Structure 分離

- `/episodes/ep02_structure.yaml` を新設
  - 旧校舎地下雨水槽構造
  - 老朽化破断による危機転化
  - 物理救出前提ルール
- EP固有構造を本体Configから分離

---

### 🧠 Structural Impact

- 真魚のキャラクターエンジンを「敵意型」から「救済型」へ刷新
- 三者構造（真魚／隼太／みずは）の力学を再定義
- 制度との長期関係アークを確定
- 魔法倫理を心理制約レイヤーへ移行

---

### ⚠️ Breaking Changes

- 氷川真魚の旧設定（復讐・否定）は無効
- 既存EP01以前の描写と齟齬が生じる場合は再確認が必要
