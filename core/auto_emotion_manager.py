from datetime import datetime
from core.emotional_memory import EmotionalMemory

class AutoEmotionManager:
    def __init__(self, emotion_manager):
        self.emotion_manager = emotion_manager
        self.emotional_memory = EmotionalMemory()

        # English emotional vocabulary
        self.positive_words = ["love you", "thank you", "great", "awesome", "best", "appreciate it", "cool", "nice"]
        self.negative_words = ["shut up", "bad", "terrible", "damn", "hate", "stupid", "broken", "sad"]
        self.surprise_words = ["i did it", "big achievement", "finished the project", "new record", "i won", "unbelievable"]

    def update_emotion(self, user_message: str):
        self._update_by_time()
        self._update_by_message(user_message)

    def _update_by_time(self):
        hour = datetime.now().hour

        if 0 <= hour < 6:
            self.emotion_manager.set_emotion("tired")
        elif 6 <= hour < 12:
            self.emotion_manager.set_emotion("happy")
        elif 12 <= hour < 18:
            self.emotion_manager.set_emotion("neutral")
        else:
            self.emotion_manager.set_emotion("formal")

    def _update_by_message(self, message: str):
        lowered = message.lower()

        if any(word in lowered for word in self.positive_words):
            self.emotional_memory.update("user", "happy")
        elif any(word in lowered for word in self.negative_words):
            self.emotional_memory.update("user", "sad")
        elif any(word in lowered for word in self.surprise_words):
            self.emotional_memory.update("user", "surprised")

        dominant_emotion = self.emotional_memory.get("user")
        if dominant_emotion:
            self.emotion_manager.set_emotion(dominant_emotion)
