import time
from core.sr_offline import listen_offline
from core.speak import speak
from intents.intent_classifier import IntentClassifier
from intents.intent_responses import get_response
from skills.commands import process_command

def is_meaningful_command(text: str) -> bool:
    """Check if the input is long and meaningful enough."""
    return len(text.strip().split()) >= 2 or len(text.strip()) > 10

def main():
    print("Richard is listening for commands... (say 'stop' to interrupt)")
    user_id = "user1"

    intent_clf = IntentClassifier()
    if intent_clf.model is None:
        intent_clf.train()

    try:
        while True:
            command = listen_offline()
            if not command:
                continue

            # نادیده گرفتن ورودی‌های کوتاه یا نامفهوم
            if not is_meaningful_command(command):
                print(f"[Ignored] Too short or unclear input: '{command}'")
                continue

            if "stop" in command.lower():
                speak("Goodbye! Richard is shutting down.")
                break

            try:
                intent = intent_clf.predict(command)
                print(f"[Intent] Predicted intent: {intent}")

                if isinstance(intent, dict):
                    intent = intent.get("intent", "unknown")

                if intent in ["time", "date", "wiki"]:
                    response = process_command(command, user_id)
                else:
                    response = get_response(intent)

                if response == "I didn't understand what you said.":
                    response = process_command(command, user_id)

            except Exception as e:
                response = process_command(command, user_id)

            speak(response)

    except KeyboardInterrupt:
        print("\n[Shutdown] Richard terminated via keyboard.")
    finally:
        print("[System] Cleanup complete.")

if __name__ == "__main__":
    total_start = time.time()
    speak("Hello, this is Richard speaking. I'm ready to serve you.")
    main()
    print(f"TOTAL RESPONSE TIME: {time.time() - total_start:.2f} sec")
