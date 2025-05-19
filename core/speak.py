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
