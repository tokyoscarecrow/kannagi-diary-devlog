本プロジェクトでは、Config を
「設定一覧」ではなく
**生成・評価・修正を制御する設計書**
として扱っている。

例えば、config_v2.2_working.yml では、

- キャラクターに change_arc を持たせ
- magic / surveillance / taboo_policy を
  物語制約として明示
- evaluation 項目を Config 内に定義

することで、
生成文のブレと後工程のレビューコストを抑制している。

