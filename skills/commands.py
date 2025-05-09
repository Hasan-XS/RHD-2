# skills/commands.py

from datetime import datetime
from core.context_manager import AdvancedContextManager
from intents.intent_classifier import IntentClassifier
from skills.wikipedia_qa import get_wikipedia_answer

# Initialize components
context_manager = AdvancedContextManager()
classifier = IntentClassifier()

def clear_and_return(user_id: str, msg: str) -> str:
    context_manager.clear_context(user_id)
    return msg

def handle_incomplete_question(command: str, user_id: str) -> str:
    context_manager.update_context(user_id, {
        "intent": "question",
        "stage": "awaiting_details",
        "partial_question": command,
        "last_updated": datetime.now()
    })
    return "Could you ask your question more clearly?"

def handle_contextual_stage(command: str, user_id: str, context: dict) -> str:
    prev_intent = context.get("intent")
    stage = context.get("stage")

    if prev_intent == "question" and stage == "awaiting_details":
        full_question = f"{context.get('partial_question', '')} {command}"
        response = get_wikipedia_answer(full_question)
        context_manager.clear_context(user_id)
        return response

    return None

def process_command(command: str, user_id: str = "default_user") -> str:
    if not command:
        return "No command received."

    lower_command = command.lower()
    current_context = context_manager.get_context(user_id)
    intent = classifier.predict(command)
    print(f"Identified Intent: {intent} | Context: {current_context}")

    if current_context:
        contextual_response = handle_contextual_stage(command, user_id, current_context)
        if contextual_response:
            return contextual_response

    # Intent handlers
    def get_time():
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    def get_date():
        return f"Today is {datetime.now().strftime('%Y-%m-%d')}."

    def goodbye():
        return clear_and_return(user_id, "See you later! Call me anytime.")

    intent_handlers = {
        "greeting": lambda: "Hello friend! Welcome back.",
        "time": get_time,
        "date": get_date,
        "thanks": lambda: "You're welcome!",
        "goodbye": goodbye,
        "wiki": lambda: (
            get_wikipedia_answer(command)
            if len(command.split()) >= 4
            else handle_incomplete_question(command, user_id)
        ),
    }

    response = intent_handlers.get(intent, lambda: "I'm not sure I understood. Can you rephrase that?")()
    context_manager.update_context(user_id, {
        "intent": intent,
        "last_updated": datetime.now()
    })

    return response
