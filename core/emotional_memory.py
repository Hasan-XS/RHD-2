import random

responses = {
    "happy": [
        "You're the best friend ever! 🌟",
        "I'm so glad to be with you! 😊",
        "You put a smile on my face! 😁"
    ],
    "sad": [
        "I'm sorry that happened... 😔",
        "I'm here whenever you need me. 🫂",
        "Wanna talk about it?"
    ],
    "tired": [
        "Let's take a break. 💤",
        "Feeling tired? I get that too sometimes. 😴",
        "How about a cup of tea? 🍵"
    ],
    "surprised": [
        "Wooooow! That was amazing! 😲🔥",
        "I can't believe you did that! 🤯",
        "You're a genius! 😍"
    ],
    "neutral": [
        "Alright, buddy! 👍",
        "I'll do whatever you say. 😎",
        "At your service."
    ],
    "formal": [
        "Your command has been received. 🙇‍♂️",
        "With utmost respect, it's done.",
        "Your request has been executed."
    ],
    "informal": [
        "You're awesome, bro! 😎",
        "Damn, you're so cool! 🔥",
        "Always got your back, dude. 🤜🤛"
    ]
}

default_response = "I’m not sure what to say… but I’m here with you. 🤖"

def get_random_emotional_response(emotion: str, intensity: float = 0.5, context: str = "default") -> str:
    """
    Returns an emotional response based on emotion, intensity, and context.
    
    :param emotion: The current emotion (e.g. 'happy', 'sad', 'neutral')
    :param intensity: A float between 0.0 and 1.0 indicating how strong the emotion is
    :param context: The style of communication: 'formal', 'informal', or 'default'
    """
    base_responses = responses.get(emotion, None)

    if not base_responses:
        return default_response

    if intensity > 0.7:
        chosen = random.choice(base_responses)
    elif intensity < 0.3:
        chosen = random.choice(base_responses[:2]) if len(base_responses) > 1 else base_responses[0]
    else:
        chosen = random.choice(base_responses)

    if context == "formal" and emotion != "formal":
        chosen = "With respect: " + chosen

    return chosen

class EmotionalMemory:
    def __init__(self):
        self.memory = {}

    def update(self, user_id: str, emotion: str):
        self.memory[user_id] = emotion

    def get(self, user_id: str) -> str:
        return self.memory.get(user_id, "neutral")

    def clear(self, user_id: str):
        if user_id in self.memory:
            del self.memory[user_id]
