# core/sr_offline.py

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
timeout = 5  # seconds to wait for user input

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
        start_time = time.time()
        result_text = ""

        while True:
            if time.time() - start_time > timeout_sec:
                if result_text:
                    print(f"[Final Result]: {result_text}")
                    return result_text
                else:
                    print("Timeout reached. No speech detected.")
                    return ""

            try:
                data = q.get(timeout=1)
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
            else:
                partial = json.loads(rec.PartialResult()).get("partial", "").strip()
                if partial and partial != result_text:
                    result_text = partial
                    print(f"(Partial): {partial}")
