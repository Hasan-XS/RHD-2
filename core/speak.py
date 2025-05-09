# core/speak.py

import pyttsx3

engine = pyttsx3.init()

# انتخاب صدای نزدیک به JARVIS
def configure_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if "male" in voice.name.lower() or "david" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # تنظیمات صدا
    engine.setProperty('rate', 155)   # سرعت مناسب
    engine.setProperty('volume', 1.0) # صدای کامل

configure_voice()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()


# import pyttsx3
# from core.emotion_manager import EmotionManager

# engine = pyttsx3.init()
# emotion_manager = EmotionManager()

# def adjust_voice_by_emotion():
#     emotion = emotion_manager.get_emotion()
    
#     rate = 150
#     volume = 1.0

#     if emotion == "happy":
#         rate = 190
#         volume = 1.0
#     elif emotion == "sad":
#         rate = 120
#         volume = 0.7
#     elif emotion == "tired":
#         rate = 100
#         volume = 0.6
#     elif emotion == "formal":
#         rate = 140
#         volume = 0.9
#     elif emotion == "informal":
#         rate = 170
#         volume = 1.0
#     elif emotion == "surprised":
#         rate = 200
#         volume = 1.0
#     else:
#         rate = 150
#         volume = 1.0

#     engine.setProperty('rate', rate)
#     engine.setProperty('volume', volume)

# def speak(text: str):
#     adjust_voice_by_emotion()
#     engine.say(text)
#     engine.runAndWait()

# speak.py
# speak.py
# speak.py
# import asyncio
# import time
# import edge_tts
# from playsound import playsound
# import uuid
# import os

# VOICE = "en-US-GuyNeural"  # صدای پیش‌فرض؛ قابل تغییر

# async def speak_text_async(text):
#     """ذخیره و پخش گفتار تولید شده"""
#     file_name = f"temp_{uuid.uuid4()}.mp3"
#     try:
#         start = time.time()
#         communicate = edge_tts.Communicate(text, VOICE)
#         await communicate.save(f"voices/{file_name}")
#         playsound(f"voices/{file_name}")
#         os.remove(f"voices/{file_name}")
#         end = time.time()
#         print(f"SPEAK TOOK: {end - start:.2f} seconds")
#     except Exception as e:
#         print(f"[SPEAK ERROR] {e}")

# def speak(text):
#     """اجرای همزمان گفتار برای محیط‌های sync و async"""
#     try:
#         loop = asyncio.get_running_loop()
#     except RuntimeError:
#         loop = None

#     if loop and loop.is_running():
#         asyncio.create_task(speak_text_async(text))
#     else:
#         asyncio.run(speak_text_async(text))
