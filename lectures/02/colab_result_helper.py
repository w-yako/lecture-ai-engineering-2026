# セクション7の後に、Colabの新しいコードセルへコピーして実行する。
# trainer.state.log_history から宿題に必要な最終Lossと学習時間を抽出する。
from pathlib import Path
import json
import shutil

history = trainer.state.log_history
losses = [entry for entry in history if "loss" in entry]
summaries = [entry for entry in history if "train_runtime" in entry or "train_loss" in entry]
last_loss = losses[-1]["loss"] if losses else None
summary = summaries[-1] if summaries else {}

path = WORK / "result.json"
if not path.is_file():
    raise FileNotFoundError(f"セクション7のresult.jsonがありません: {path}")

result = json.loads(path.read_text(encoding="utf-8"))
result["training_metrics"] = {
    "last_logged_loss": last_loss,
    "mean_train_loss": summary.get("train_loss"),
    "training_seconds": summary.get("train_runtime"),
    "steps": trainer.state.global_step,
}
path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

if USE_DRIVE:
    target = Path(CONFIG["drive_dir"]) / "result.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    print("Google Driveに保存:", target)

print("エポック数:", CONFIG["num_train_epochs"])
print("学習後 format_rate:", result["after"]["format_rate"])
print("学習後 content_rate:", result["after"]["content_rate"])
print("最終Loss:", last_loss)
print("学習時間（秒）:", summary.get("train_runtime"))
print("学習ステップ数:", trainer.state.global_step)
