# 第2回の宿題：基礎（20エポックと10エポックを比較）

**現状：answer.md は未完成の下書きです。学習を2条件で実行した実測値が必要です。**

## 実験①：20エポック

1. [第2回ノートブック](https://colab.research.google.com/github/w-yako/lecture-ai-engineering-2026/blob/main/notebooks/lora_format_tuning.ipynb) をColabで開き「ファイル → ドライブにコピーを保存」。
2. 「ランタイム → ランタイムのタイプを変更」でT4 GPUを選択。
3. 設定（CONFIG）のnum_train_epochsを20のまま、work_dirを「/content/qlora_lab_20ep」、drive_dirを「/content/drive/MyDrive/aie2026/qlora_20ep」に設定し、USE_DRIVE=Trueとする。ほかの学習条件は変更しない。
4. セクション0〜7を上から実行し、[colab_result_helper.py](colab_result_helper.py) のコードをColabの新しいコードセルで実行。
5. GoogleドライブのMyDrive/aie2026/qlora_20ep/result.jsonを確認する。

## 実験②：10エポック

1. 「ランタイム → セッションを再起動」を実行する。学習後のadapterが残った状態で再実験しない。
2. CONFIGのnum_train_epochsを10、work_dirを「/content/qlora_lab_10ep」、drive_dirを「/content/drive/MyDrive/aie2026/qlora_10ep」とする。USE_DRIVE=Trueのまま。
3. セクション0〜7と同じ補助セルを再実行し、MyDrive/aie2026/qlora_10ep/result.jsonを保存する。

## 提出前のチェック

次を両方のresult.jsonから読み取り、[answer.md](answer.md) の表を更新する。

| 項目 | result.jsonのキー |
| --- | --- |
| 学習後の形式遵守率 | after.format_rate |
| 学習後の内容正解率 | after.content_rate |
| 最終Loss | training_metrics.last_logged_loss |
| 学習時間（秒） | training_metrics.training_seconds |
| 学習ステップ数 | training_metrics.steps |

学習結果に即して考察を書く。講師の参考データは自分の結果として記載しない。PRを完成状態にするのはこの後。Colabは終了後「ランタイム → ランタイムを接続解除して削除」する。
