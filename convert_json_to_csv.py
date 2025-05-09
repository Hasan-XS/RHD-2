import json
import csv

json_path = "models/intent.json"  # مسیر فایل JSON خودت رو بنویس
csv_path = "intents/intents.csv"  # مسیر خروجی CSV

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(csv_path, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["text", "intent_name"])  # سرستون‌ها

    for intent, texts in data.items():
        for text in texts:
            writer.writerow([text, intent])
