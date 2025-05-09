# from TTS.utils.synthesizer import Synthesizer
# import sounddevice as sd

# # 🔧 ساخت نمونه‌ی سینتی‌سایزر با مدل دانلودشده
# synthesizer = Synthesizer(
#     tts_checkpoint="tts_models/models/tacotron2_ddc/tts-model_file.pth",
#     tts_config_path="tts_models/models/tacotron2_ddc/tts-config.json",
#     vocoder_checkpoint="tts_models/models/tacotron2_ddc/vocoder-model_file.pth.tar",
#     vocoder_config="tts_models/models/tacotron2_ddc/vocoder-config.json",
#     use_cuda=False
# )

# # 🎤 جمله مورد نظر
# text = "Hello sir. All systems are online."

# # 🎧 تولید صدا
# wav = synthesizer.tts(text)

# # 💾 ذخیره به فایل (اختیاری)
# synthesizer.save_wav(wav, "jarvis_output.wav")

# # 🔊 پخش صدا
# sd.play(wav, 22050)
# sd.wait()
# import time

# import asyncio
# import edge_tts
# from playsound import playsound

# VOICE = "en-US-GuyNeural"
# OUTPUT_FILE = "output.mp3"

# loop = asyncio.get_event_loop()

# async def speak_text_async(text):
#     communicate = edge_tts.Communicate(text, VOICE)
#     await communicate.save(OUTPUT_FILE)
#     playsound(OUTPUT_FILE)


# def speak(text):
#     start = time.time()
#     asyncio.run(speak_text_async(text))
#     end = time.time()
#     print(f"SPEAK TOOK: {end - start:.2f} seconds")


# if __name__ == "__main__":
#     total_start = time.time()
#     speak("Hello, this is Richard speaking. I'm ready to serve you.")
#     print(f"TOTAL RESPONSE TIME: {time.time() - total_start:.2f} sec")


# import sounddevice as sd
# import vosk
# import queue
# import json

# model = vosk.Model("models/vosk-model-small-en-us-0.15")
# q = queue.Queue()

# def callback(indata, frames, time, status):
#     q.put(bytes(indata))

# samplerate = 16000
# with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
#                        channels=1, callback=callback):
#     print("Say something...")

#     rec = vosk.KaldiRecognizer(model, samplerate)
#     while True:
#         data = q.get()
#         if rec.AcceptWaveform(data):
#             result = json.loads(rec.Result())
#             print(result.get("text"))


# from datasets import load_dataset
# import json
# import pandas as pd

# # مسیر فایل محلی
# df = pd.read_csv("ccc/train.csv")

# print(df.head())


# # ساختار دیکشنری برای intentها
# intents = {}



# for _, row in df.iterrows():
#     intent = row["intent"]
#     intent_name = row["intent_name"]
#     domain_name = row["domain_name"]
#     text = row["text"]
    

#     intents.setdefault(intent_name, []).append(domain_name)


# # ذخیره در فایل JSON
# with open("test.json", "w", encoding="utf-8") as f:
#     json.dump(intents, f, indent=4, ensure_ascii=False)

# print(intents.columns)

# print("✅ فایل intents.json ساخته شد!")


# import pandas as pd
# import json

# # مسیر فایل پارکت (اگه جای دیگه گذاشتی، مسیر رو تغییر بده)
# parquet_path = "models/train-00000-of-00001.parquet"

# # فایل رو بخون
# df = pd.read_parquet(parquet_path)

# # بررسی کن چه ستون‌هایی داریم
# print("Columns:", df.columns)

# # حالا ساختار intent‌ها رو بسازیم
# intents = {}

# for _, row in df.iterrows():
#     intent = row["intent"]
#     text = row["text"]
    

#     if intent not in intents:
#         intents[intent] = []

#     intents[intent].append(text)

# # حالا ساختار JSON نهایی
# intent_data = {
#     "intents": []
# }

# for intent, patterns in intents.items():
#     intent_data["intents"].append({
#         "tag": intent,
#         "patterns": patterns,
#         "responses": ["..."]  # بعداً می‌تونی این قسمت رو با پاسخ‌های دلخواه پر کنی
#     })

# # ذخیره به فایل
# with open("models/intent.json", "w", encoding="utf-8") as f:
#     json.dump(intent_data, f, ensure_ascii=False, indent=4)

# print("✅ تبدیل با موفقیت انجام شد و در فایل intents.json ذخیره شد.")

# from core.nlp import NLPProcessor

# nlp_processor = NLPProcessor()
# keywords = nlp_processor.extract_keywords("I'm working on an advanced AI assistant that talks and listens.")
# print(keywords)

# import pandas as pd
# import json

# # خواندن فایل CSV
# df = pd.read_csv("ccc/train.csv")

# # ساختار نهایی فقط شامل intent_name و لیستی از text‌ها
# intents = {}

# for _, row in df.iterrows():
#     intent_name = row["intent_name"]
#     text = row["text"]

#     # اگر intent_name وجود نداشت، اضافه‌اش کن
#     if intent_name not in intents:
#         intents[intent_name] = []

#     # اضافه کردن text به لیست مربوط به intent_name
#     intents[intent_name].append(text)

# # ذخیره در فایل JSON
# with open("models/intent.json", "w", encoding="utf-8") as f:
#     json.dump(intents, f, indent=4, ensure_ascii=False)

# print("✅ فایل intents.json فقط با intent_name و text ساخته شد!")

# import pandas as pd
# import json

# # مسیر فایل محلی
# df = pd.read_csv("ccc/train.csv")

# # ساختار دیکشنری دقیق برای intent ها
# intents = {}

# for _, row in df.iterrows():
#     # intent = row["intent"]
#     intent_name = row["intent_name"]
#     domain_name = row["domain_name"]
#     text = row["text"]
    
#     # بررسی اینکه آیا intent در دیکشنری موجود است یا نه
#     if intent_name not in intents:
#         intents[intent_name] = {}

#     # if intent_name not in intents[intent_name]:
#     #     intents[intent_name][intent_name] = {}

#     if domain_name not in intents[intent_name]:
#         intents[intent_name][domain_name] = []

#     # اضافه کردن متن به دامین خاص
#     intents[intent_name].append(text)

# # ذخیره در فایل JSON
# with open("models/intent.json", "w", encoding="utf-8") as f:
#     json.dump(intents, f, indent=4, ensure_ascii=False)

# print("✅ فایل test.json ساخته شد!")

# import pandas as pd

# # بارگذاری دیتاست
# intents = pd.read_csv("ccc/train.csv")


# # بررسی ستون‌ها برای اطمینان
# print("ستون‌های موجود:", intents.columns.tolist())

# # نمایش تمام intent_name‌ها
# unique_intents = intents['intent_name'].unique()
# print("\n📌 لیست تمام intent_name‌ها:")
# for intent in unique_intents:
#     print(f"- {intent}")

# # نمایش تمام domain_name‌ها
# unique_domains = intents['domain_name'].unique()
# print("\n📌 لیست تمام domain_name‌ها:")
# for domain in unique_domains:
#     print(f"- {domain}")




# test_intent.py
from intents.intent_classifier import IntentClassifier

model = IntentClassifier()

while True:
    text = input("You: ")
    if text.lower() in ["exit", "quit"]:
        break
    intent = model.predict(text)
    print(f"Detected intent: {intent}")
