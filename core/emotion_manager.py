from collections import deque

class EmotionManager:
    def __init__(self, history_size=5):
        self.valid_emotions = ["happy", "sad", "tired", "formal", "informal", "neutral", "surprised"]
        self.current_emotion = {"type": "neutral", "intensity": 0.5}
        self.emotion_history = deque(maxlen=history_size)

    def set_emotion(self, emotion_type: str, intensity: float = 0.5):
        """
        Sets the current emotion with optional intensity.
        """
        if emotion_type not in self.valid_emotions:
            raise ValueError(f"Invalid emotion type: {emotion_type}")
        
        intensity = max(0.0, min(1.0, intensity))  # Clamp intensity to [0.0, 1.0]
        self.current_emotion = {"type": emotion_type, "intensity": intensity}
        self.emotion_history.append(self.current_emotion)

    def get_emotion(self):
        """
        Returns the current emotion as a dictionary.
        """
        return self.current_emotion

    def get_emotion_type(self):
        """
        Returns just the emotion type string.
        """
        return self.current_emotion["type"]

    def get_emotion_history(self):
        """
        Returns a list of past emotions (up to history_size).
        """
        return list(self.emotion_history)

    def reset_emotion(self):
        """
        Resets the emotion back to neutral.
        """
        self.set_emotion("neutral", 0.5)
