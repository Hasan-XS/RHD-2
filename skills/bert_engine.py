from transformers import pipeline

# Set up the question-answering model
question_answerer = pipeline(
    "question-answering", model="distilbert-base-uncased-distilled-squad"
)

# Conversation history storage
conversation_history = []

# Initial context for QA
initial_context = (
    "OpenAI is an AI research and deployment company. "
    "Our mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. "
    "We will build safe and beneficial AGI, or help others achieve this outcome."
)

# Function to process a question using conversation history
def ask_richard(question):
    try:
        # Use conversation history as context if available
        if conversation_history:
            context = " ".join([f"Q: {q} A: {a}" for q, a in conversation_history])
        else:
            context = initial_context

        # Get the answer from the model
        response = question_answerer(question=question, context=context)
        answer = response["answer"]

        # Update the conversation history
        conversation_history.append((question, answer))

        # Limit history to the last 5 interactions
        if len(conversation_history) > 5:
            conversation_history.pop(0)

        return answer
    except Exception as e:
        print(f"Error processing the question: {e}")
        return "I'm sorry, I couldn't process your question."


# Example usage
question1 = "What is OpenAI?"
answer1 = ask_richard(question1)
print(f"Richard's Answer: {answer1}")

question2 = "What is its mission?"
answer2 = ask_richard(question2)
print(f"Richard's Answer: {answer2}")
