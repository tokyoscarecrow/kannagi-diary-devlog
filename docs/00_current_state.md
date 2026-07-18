# Current Project State

## Overview

This document defines the **current authoritative state** of the project.

It provides a quick reference for:
- Which configs are active
- What structure is currently being worked on
- What the project is focusing on at this stage

If you are new to the repository, start here.

---

## Active Core Configs (Authoritative)

The following files define the current system.

### Top-Level (Non-negotiable)

- `raw/Config/PROJECT_MASTER_CONTEXT.yaml`
- `raw/Config/GLOBAL_CONFIG.yaml`

These define:
- What the project is
- How the system must behave

---

### Domain Configs (Active)

- `raw/Config/config_v2.5.yaml`
- `raw/Config/addressing_rules.yaml`

These define:
- Character behavior
- World rules
- Interaction consistency

---

### Structure Definition

- `raw/episodes/ep02_structure.yaml`

This defines:
- Scene structure (SC)
- Narrative progression
- Tension design

---

## Current Episode Focus

### EP02 (Active Development Phase)

The project is currently focused on:

> **Structural design and validation of Episode 02**

Key elements:

- Scene-based narrative architecture (SC system)
- Structural trap design (misdirection and perception control)
- Validation of narrative constraints through execution

---

## Key Design Concepts (Current Stage)

### 1. Narrative as Structure

Narrative is treated as:
- A sequence of constrained units (SC)
- Not as free-form writing

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
- Conflicts must be reported, not silently resolved

---

### 4. Trap-Oriented Design (EP02)

Current narrative design includes:

- Intentional misdirection
- Explicitly defined “false assumptions”
- Reader/player perception control

---

## Current Constraints

- Structure cannot be modified without approval
- AI operates only within defined constraints
- All generation must respect Config hierarchy

---

## Status Summary

- Multi-layer config system: **Active**
- GLOBAL_CONFIG: **Implemented**
- PROJECT_MASTER_CONTEXT: **Implemented**
- EP02 structure: **Defined and under validation**
- Governance rules: **In operation**

---

## Next Direction

The project will continue focusing on:

- Stabilizing long-form narrative generation
- Expanding structural design patterns
- Testing governance under complex scenarios
- Integrating narrative philosophy into config systems

---

## Notes

This document represents the **current state**, not the full history.

For historical changes:
- See `/archive`
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

---

## 有効なコアConfig（正本）

現在のシステムを構成する主要ファイルは以下の通り。

---

### 最上位（不変）

- `raw/Config/PROJECT_MASTER_CONTEXT.yaml`
- `raw/Config/GLOBAL_CONFIG.yaml`

これらは：

- プロジェクトの定義
- 生成ルールの規律

を決定する。

---

### ドメインConfig（有効）

- `raw/Config/config_v2.5.yaml`
- `raw/Config/addressing_rules.yaml`

これらは：

- キャラクター挙動
- 世界設定
- 会話・呼称の一貫性

を定義する。

---

### 構造定義

- `raw/episodes/ep02_structure.yaml`

これにより：

- シーン構造（SC）
- 進行設計
- テンション設計

が規定される。

---

## 現在のエピソード焦点

### EP02（開発中）

現在の主目的は：

> **Episode 02 における構造設計と検証**

主な要素：

- SCベースのナラティブ構造
- 認知誘導（トラップ）設計
- 制約に基づく物語生成の検証

---

## 現在の設計思想

### 1. ナラティブ＝構造

物語は：

- 制約された単位（SC）の連鎖

として扱う。

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
- 矛盾は報告する（黙って修正しない）

---

### 4. トラップ設計（EP02）

現在の設計では：

- 意図的な誤誘導
- 「嘘」の明文化
- 認知操作

を含む構造を採用している。

---

## 現在の制約

- 構造変更は禁止（承認なし）
- AIは制約内でのみ動作
- すべての生成はConfig階層に従う

---

## 状態まとめ

- 多層Config構造：運用中
- GLOBAL_CONFIG：導入済み
- PROJECT_MASTER_CONTEXT：確定
- EP02構造：定義済み・検証中
- ガバナンス：運用中

---

## 今後の方向

- 長編生成の安定化
- 構造設計の拡張
- ガバナンスの実証
- ナラティブ思想の形式化

---

## 注記

本ドキュメントは**現時点の状態**を示すものであり、履歴ではない。

履歴は以下を参照：

- `/archive`
- 各Configのバージョン履歴

