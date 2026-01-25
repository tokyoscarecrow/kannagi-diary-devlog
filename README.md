# かんなぎダイアリー  
*KANNAGI DIARY*

ナラティブ制作における  
**設計・判断・レビュー工程を記録し、再現可能な形で公開する**  
制作実験ログ兼・方法論リポジトリ。

---

## 📖 作品について

『かんなぎダイアリー』は、**現代日本を舞台にした学園ファンタジー**です。

**あらすじ（第一章）**
特種能力者として政府の監視下にある高校生・隼太の平凡な日常に、
転校生・真魚が現れたことで、隠された過去が動き出す──

**制作方針**
- 物語本文は100% AI生成（人間は一文字も書かない）
- YAMLベースのConfig駆動型生成
- Scene Card → Tension Curve → Clinical Review の構造的プロセス
- 成功だけでなく失敗・廃案も含めて記録公開

※完成した物語は下記noteマガジンで公開中

---

## このリポジトリは何か
**『かんなぎダイアリー』** は、  
オリジナル企画の制作過程において行われた

- 構成設計
- シーン分解
- テンション設計
- クリニカルレビュー

といった **ナラティブ制作工程そのもの**を対象にした  
**研究記録・公開ドキュメント**です。

> 物語そのものではなく  
> 「どう設計し、どう判断し、どう修正したか」を扱います。

---

## 本文（成果物）について
本企画で制作された **完成した物語本文（成果物）** は  
**GitHub では公開していません**。

- 📖 **ブログ**：読まれるための成果物（本文）
- 🧪 **GitHub**：その本文を生み出すための設計・判断・検証の記録

という役割分担を採用しています。

---

## 公開方針（要約）
本リポジトリは、以下を原則とします。

- 成果物だけでなく、途中経過・失敗・廃案も含めて公開する
- 後付けの成功談ではなく、実際の判断履歴を残す
- 情報は「編集済み」と「一次資料」に分けて整理する

これは完成形のノウハウ集ではなく、  
**制作と思考のログ（メモランダム）**です。

---

## Quick Start（はじめての方へ）

1. **現在の推奨構成を確認する**  
   → [`docs/00_current_state.md`](docs/00_current_state.md)

2. **全体の工程と考え方を把握する**  
   → [`docs/01_overview.md`](docs/01_overview.md)

3. **関心のある工程を読む**  
   - Config 設計 → [`docs/10_config_design.md`](docs/10_config_design.md)
   - シーンカード → [`docs/20_scene_cards.md`](docs/20_scene_cards.md)
   - テンション曲線 → [`docs/30_tension_curve.md`](docs/30_tension_curve.md)
   - クリニカルレビュー → [`docs/40_clinical_review.md`](docs/40_clinical_review.md)

---

# 📖 関連リンク

### 完成した物語を読む
📚 [かんなぎダイアリー AI生成（note）](https://note.com/tokyoscarecrow/m/m83debbbe25d4)
- 第一章　全８話公開中
- YAMLファイルでコントロールしたAI生成による物語

### 制作過程を知る
🔬 [『かんなぎダイアリー』開発記（note）](https://note.com/tokyoscarecrow/m/mb2297738eabf)
- Config設計からシーン生成までの詳細プロセス
- 判断基準や試行錯誤の記録

### 技術資料・生データ
💾 **このGitHubリポジトリ**
- YAMLファイル、設計ドキュメント、廃案資料など

---

## 📁 ディレクトリ構成
```
├── docs/                              # 編集済みドキュメント（推奨読み物）
│   ├── 00_current_state.md            # 現在の到達点・進行状況（更新点の要約）
│   ├── 01_overview.md                 # 全体概要／制作思想／方法論サマリ
│   │
│   ├── 10_config_design.md            # Config設計の考え方
│   ├── 20_scene_cards.md              # シーンカード手法の解説
│   ├── 30_tension_curve.md             # テンション設計とEP01検証（確定）
│   │
│   ├── 40_clinical_review.md           # クリニカルレビュー手法（一般論）
│   │
│   ├── 90_ep01_review.md               # EP01 トータルレビュー（評価あり）
│   └── 95_ep01_re_review.md            # EP01 破壊的レビュー（ダメ出しのみ）
│
├── raw/                               # 一次資料（生ログ・未編集・思考の源流）
│   ├── config/                        # 現在使用している Config 最新版（YAML）
│   ├── scene_cards/                   # 現在使用している Scene Card 最新版
│   ├── world_foundation/              # 世界観成立の一次テキスト
│   │   ├── world_concept_initial.md
│   │   └── README.md
│   ├── decision_logs/                 # 判断履歴（順序変更・方針転換など）
│   │   ├── EP01_SC07_SC08_reorder.md
│   │   └── README.md
│
├── archive/                           # 廃案・過去バージョン・比較用
│   ├── generated_drafts/              # 採用されなかったAI生成本文
│   ├── scene_cards/                   # 過去版シーンカード
│   └── config/                        # 過去版Config
│
├── templates/                         # 再利用可能なテンプレート
│   ├── config_template.yml            # 抽象化されたConfigテンプレ
│   ├── scene_card_template.yml        # シーンカードテンプレ
│   └── review_templates/              # レビュー用テンプレ群
│
├── characters/                        # キャラクター設定資料
│   └── 00_characters_initial_draft.md # 最初期キャラ設定原文（一次資料）
│
├── diagrams/                          # 図解・構造図（任意・将来拡張）
│   ├── narrative_flow_ep01.png
│   └── tension_curve_ep01.png
│
└── README.md                          # リポジトリ総合README

```

---

## 🌐 Author
Yoshida Ryo – Narrative Designer / Director  
https://dailyarts.co.jp/
