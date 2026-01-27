# 混雑状況検知システム（crowd_moniter）
このプロジェクトは食堂・お風呂などの混雑状況をリアルタイムで検知しAPIで提供表示するための最小構成です。
仕組みとしてはOPENCVでトラッキングをして重心移動による入退場判定でカウントする。

## ディレクトリ構成
git_hub  <br>
|crowd_moniter  <br>
    |--matarial <br>
    |--README.md  <br>
    |--memo.txt メモ帳  <br>
    |--list_lib.txt　依存ライブラリ一覧  <br>
    |--main.py　メイン処理  <br>
    |--detecter.py　人物検出  <br>
    |--tracker.py　トラッキング  <br>
    |--counter.py　入退場判定と人数更新  <br>
    |--apiserver.py　APIの提供  <br>
    |--db.py　DBの記録、取得  <br>
    |--config.py　設定  <br>
    |--test　テスト  <br>
    

## 使用技術について
画像認識  <br>
API(WEBアプリ)  <br>
フロントエンド  <br>
人数データの保存、取得  <br>

## 処理フロー
カメラ -> YORO　-> OPENCV　-> 人数判定　-> DB更新　-> API -> 表示

## データベース設計
テーブル名: log_deta  <br>
-id (int)  <br>
-timestamp(datetime)  <br>
-location(text)(str)  <br>
-current_count(int)  <br>
