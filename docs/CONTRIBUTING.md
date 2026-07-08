# Contributing Guide

## Commit Message Rules

このプロジェクトでは、コミットメッセージに以下の形式を使います。

```text
type: message
```

## Types

- feat: 新機能追加
- fix: バグ修正
- docs: ドキュメント更新
- style: UIや見た目の変更
- refactor: 動作を変えないコード整理
- chore: 設定・環境・雑作業
- test: テスト追加・修正

## Examples

```text
feat: Add public hub screen
feat: Add SQLite database connection
fix: Fix search result layout
docs: Update roadmap
style: Improve public UI spacing
refactor: Split search service from GUI
chore: Update requirements
test: Add search service tests
```

## Main Branch Rule

main ブランチは常に起動できる状態を保ちます。

壊れた状態では commit / push しないようにします。