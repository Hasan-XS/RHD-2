import queue
import sounddevice as sd
import vosk
import json
import time
import os

# Load Vosk model (make sure the path is correct)
MODEL_PATH = "models/vosk-model-en-us-0.22"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Vosk model not found in {MODEL_PATH}")
model = vosk.Model(MODEL_PATH)

# Configuration
samplerate = 16000
device = None  # Set specific device index if needed
blocksize = 8000
timeout = 3  # Reduced timeout to 3 seconds
last_speech_time = time.time()

# Queue for audio data
q = queue.Queue()

def callback(indata, frames, time_info, status):
    if status:
        print(f"[Status] {status}")
    q.put(bytes(indata))

def listen_offline(timeout_sec=timeout):
    print("Listening (offline mode)...")

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, device=device,
                           dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        rec.SetWords(True)
        result_text = ""

        while True:
            try:
                data = q.get_nowait()  # Non-blocking, immediate check
            except queue.Empty:
                continue

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if len(text.split()) >= 1:
                    print(f"You said (offline): {text}")
                    return text
                else:
                    print("[Ignored] Input too short.")
                    last_speech_time = time.time()
            else:
                partial = json.loads(rec.PartialResult()).get("partial", "").strip()
                if partial and partial != result_text:
                    result_text = partial
                    print(f"(Partial): {partial}")
                    last_speech_time = time.time()

            # Check if user stopped speaking
            if time.time() - last_speech_time > 1.5 and result_text:
                print(f"[Final from Partial]: {result_text}")
                return result_text

            # Timeout condition
            if time.time() - last_speech_time > timeout_sec:
                if result_text:
                    print(f"[Final Result]: {result_text}")
                    return result_text
                else:
                    print("Timeout reached. No speech detected.")
                    return ""
