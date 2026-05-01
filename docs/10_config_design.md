# Config Design

## Overview

This project does not treat narrative as text generation, but as a **structured system design problem**.

The goal is not to “write a story,” but to:
- Define the **constraints under which a story emerges**
- Ensure consistency across long sessions
- Enable reproducible narrative generation

To achieve this, the system is organized into multiple layers of Configs with clearly separated roles.

---

## Config Architecture (Current)

The current system consists of three primary layers:

### 1. PROJECT_MASTER_CONTEXT (What to build)

This is the **top-level, non-negotiable rule set**.

- Defines world assumptions, invariants, and core constraints
- Contains elements that must **never drift or be reinterpreted**
- Acts as the **reference anchor across all sessions**

Examples:
- Nature of “magicians” (かんなぎ)
- Core world rules
- Narrative invariants

→ This layer answers:
> *“What is this project fundamentally about?”*

---

### 2. GLOBAL_CONFIG (How to build)

This layer defines **generation discipline and behavior rules**.

- Prevents structural drift over long conversations
- Defines how the AI must behave when generating content
- Introduces **governance rules** for structure changes

Key responsibilities:
- Scene card integrity
- Structural consistency enforcement
- Conflict reporting (no silent fixes)
- Anti-drift mechanisms

Important rule:
> The system must NOT modify structure without explicit approval.

→ This layer answers:
> *“How should the system behave while generating narrative?”*

---

### 3. Domain Configs (Detailed constraints)

These are modular configs that define specific aspects:

- MAGOSHA_COMMON_RULES
- CHARACTER_LAYER
- HUMAN_BEHAVIOR_CONSTRAINTS
- WORLD_HISTORY_LAYER
- addressing_rules (speech consistency)

Each config:
- Is independently versioned
- Defines a specific domain of constraints
- Works together under GLOBAL_CONFIG discipline

→ This layer answers:
> *“What specific rules apply to characters, world, and behavior?”*

---

## Key Design Principles

### 1. Separation of Structure and Content

- Structure (SC count, order, role) is **strictly controlled**
- Content (dialogue, description) is **flexible**

AI is allowed to:
- Generate content freely

AI is NOT allowed to:
- Split or merge scenes
- Reorder scenes
- Alter structural roles

Without explicit approval.

---

### 2. Explicit Structure Governance

All structural changes must follow:

1. Proposal  
2. Approval  
3. Application  

No exceptions.

This prevents:
- Silent drift
- Local optimization breaking global structure
- Loss of authorial control

---

### 3. Anti-Drift Design

Long AI conversations tend to degrade constraints over time.

To counter this:

- GLOBAL_CONFIG acts as a persistent rule system
- PROJECT_MASTER_CONTEXT acts as an invariant anchor
- Conflicts must be surfaced, not resolved silently

---

### 4. Narrative as Constraint Satisfaction

Narrative is treated as:

> A system where output emerges from constraints

Not from:
- improvisation
- stylistic writing alone

This allows:
- reproducibility
- analysis
- iterative refinement

---

## Evolution of the System

### Early Phase (v2.2 and before)
- Single YAML config
- Mixed structure and content rules
- High flexibility, but unstable

### Transition Phase (v2.3–v2.4)
- Separation of layers begins
- Introduction of structural documents (episode structure YAML)

### Current Phase (v2.5+)
- Full multi-layer architecture
- GLOBAL_CONFIG introduced
- PROJECT_MASTER_CONTEXT defined
- Governance rules enforced

---

## Why This Matters

Most AI-assisted writing fails because:

- Constraints degrade over time
- Structure is not enforced
- Systems rely on memory instead of design

This project attempts to solve that by:

- Designing the **structure first**
- Making rules explicit
- Treating narrative as a controlled system

---

## Current Focus

At the current stage, the project focuses on:

- Stabilizing long-form generation
- Preventing structural drift
- Designing narrative traps and misdirection structurally
- Testing governance rules in real scenarios (EP02)

---

## Future Direction

Potential expansions include:

- Tool-assisted validation of configs
- Visualization of structure (scene graphs)
- Formalization of narrative logic patterns
- Reusable narrative design frameworks

---

## Summary

This project is not about writing stories with AI.

It is about:

> Designing a system where stories can be generated **reliably, consistently, and intentionally**.

---

# Config設計（日本語版）

## 概要

本プロジェクトは、物語を「文章生成」として扱うのではなく、  
**構造システムの設計問題**として扱う。

目的は次の通り：

- 物語が生まれるための**制約を設計すること**
- 長期的な生成における一貫性を維持すること
- 再現可能なナラティブ生成を実現すること

そのために、複数のConfigレイヤーによる構造を採用している。

---

## Config構造（現行）

現在のシステムは、以下の3層で構成される。

---

### 1. PROJECT_MASTER_CONTEXT（何を作るか）

最上位の**不変ルール定義**。

- 世界観・前提・絶対条件を定義
- 再解釈や変更を許さない
- 全チャット共通の参照基準

例：
- 魔法者（かんなぎ）の定義
- 世界の基本ルール
- ナラティブ上の不変条件

→ この層は次の問いに答える：

> 「このプロジェクトは何を扱うのか？」

---

### 2. GLOBAL_CONFIG（どう作るか）

生成時の**挙動と規律を定義する層**。

- 長期生成における構造劣化を防ぐ
- AIの振る舞いを制御する
- 構造変更のガバナンスを定義する

主な役割：

- シーンカードの整合性維持
- 構造変更の制御
- 矛盾の報告（黙って修正しない）
- ドリフト防止

重要ルール：

> 構造はユーザー承認なしに変更してはならない

→ この層は次の問いに答える：

> 「生成はどのように行うべきか？」

---

### 3. ドメイン別Config（詳細制約）

各領域ごとの制約を定義する。

- MAGOSHA_COMMON_RULES
- CHARACTER_LAYER
- HUMAN_BEHAVIOR_CONSTRAINTS
- WORLD_HISTORY_LAYER
- addressing_rules

特徴：

- 独立したバージョン管理
- 領域ごとの責務分離
- GLOBAL_CONFIGの規律下で動作

→ この層は次の問いに答える：

> 「具体的にどのような制約が存在するか？」

---

## 設計原則

### 1. 構造と内容の分離

- 構造（SC数・順序・役割）は厳密に管理
- 内容（セリフ・描写）は柔軟に生成

AIが許可されること：
- 内容生成

禁止されること：
- SCの分割・統合
- 順序変更
- 構造改変（無断）

---

### 2. 構造変更ガバナンス

すべての構造変更は以下を必須とする：

1. 提案  
2. 承認  
3. 反映  

例外なし。

---

### 3. ドリフト防止設計

長期対話では制約が劣化する。

対策：

- GLOBAL_CONFIGによる制御
- PROJECT_MASTER_CONTEXTによる固定
- 矛盾は報告する（自動修正しない）

---

### 4. ナラティブ＝制約充足問題

本プロジェクトでは：

> 物語は制約から生成されるもの

と定義する。

即興や文体ではなく、

- 再現性
- 分析性
- 改善可能性

を重視する。

---

## システムの進化

### 初期（v2.2以前）
- 単一Config
- 構造と内容が混在
- 不安定

### 過渡期（v2.3–v2.4）
- 層分離開始
- 構造YAML導入

### 現行（v2.5以降）
- 多層構造確立
- GLOBAL_CONFIG導入
- PROJECT_MASTER_CONTEXT確定
- ガバナンス運用開始

---

## なぜ重要か

多くのAI生成は失敗する：

- 制約が崩壊する
- 構造が維持されない
- 設計ではなく記憶に依存する

本プロジェクトはこれを解決する試みである。

---

## 現在の焦点

- 長編生成の安定化
- 構造ドリフト防止
- 認知トラップ設計（EP02）
- ガバナンス実証

---

## 今後の展開

- Config検証ツール
- 構造可視化
- ナラティブパターン体系化
- 再利用可能フレームワーク

---

## まとめ

本プロジェクトは物語を書くものではない。

> 意図通りに物語を生成できるシステムを設計する試みである。