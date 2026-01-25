# 混雑状況検知システム（crowd_moniter）
このプロジェクトは食堂・お風呂などの混雑状況をリアルタイムで検知しAPIで提供表示するための最小構成です。
仕組みとしてはOPENCVでトラッキングをして重心移動による入退場判定でカウントする。

## ディレクトリ構成
git_hub
|crowd_moniter
    |--README.md　
    |--main.py　メイン処理
    |--detecter.py　人物検出
    |--tracker.py　トラッキング
    |--counter.py　入退場判定と人数更新
    |--apiserver.py　APIの提供
    |--db.py　DBの記録、取得
    |--config.py　設定
    |--list_lib.txt　依存ライブラリ一覧
    |--test　テスト

## 使用技術について
画像認識
API(WEBアプリ)
フロントエンド
人数データの保存、取得

## 処理フロー
カメラ -> YORO　-> OPENCV　-> 人数判定　-> DB更新　-> API -> 表示

## データベース設計
テーブル名: log_deta
-id (int)
-timestamp(datetime)
-location(text)(str)
-current_count(int)
