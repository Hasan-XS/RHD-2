import random

# پاسخ‌های پیش‌فرض برای هر نیت
intent_responses = {
    "greeting": ["Hi there! I'm here.", "Hello! How can I assist you?", "Hey buddy!"],
    "goodbye": ["Goodbye!", "See you later!", "Call me anytime you need."],
    "time": ["Let me check the time..."],
    "date": ["Let me tell you today's date..."],
    "thanks": ["You're welcome!", "No problem!", "Always here to help."],
    "wiki": ["Alright, searching now..."],
    "unknown": [
        "I didn't understand what you said.",
        "Sorry, could you repeat that?",
        "Hmm, not sure what you meant.",
    ],
}


def get_response(intent: str) -> str:
    """
    دریافت پاسخ بر اساس intent شناسایی‌شده.
    اگر intent ناشناس باشد، پاسخ پیش‌فرض بازمی‌گرداند.
    """
    return random.choice(intent_responses.get(intent, intent_responses["unknown"]))
