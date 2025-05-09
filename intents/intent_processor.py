# Standard libraries
import random
import datetime
import json

# Third-party library
import wikipedia

# Local imports
from intents.intent_classifier import IntentClassifier

# Set Wikipedia language to English
wikipedia.set_lang("en")

# Load intents
with open("intents/intents.json", encoding="utf-8") as f:
    intents = json.load(f)

# Initialize intent classifier
classifier = IntentClassifier()

def process_intent(text: str) -> str:
    """Processes the given text, predicts the intent, and returns an appropriate response."""
    intent = classifier.predict(text)

    for i in intents["intents"]:
        if i["tag"] == intent:
            if intent == "time":
                now = datetime.datetime.now()
                return now.strftime("The current time is %H:%M.")

            elif intent == "date":
                today = datetime.datetime.today()
                return today.strftime("Today's date is %Y/%m/%d.")

            elif intent == "wiki":
                try:
                    # Use the full input text as query (you can improve this with NLP)
                    query = text.strip()
                    summary = wikipedia.summary(query, sentences=2)
                    return summary
                except Exception:
                    return "Sorry, I couldn't find anything. Please ask more clearly."

            return random.choice(i["responses"])

    return "Sorry, I didn't understand that. Please try again."
