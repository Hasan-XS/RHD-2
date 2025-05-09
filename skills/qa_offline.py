# qa_offline.py

from transformers import pipeline, Pipeline

# Initialize the offline question answering pipeline
try:
    qa_pipeline: Pipeline = pipeline(
        "question-answering",
        model="distilbert-base-uncased-distilled-squad",
        tokenizer="distilbert-base-uncased-distilled-squad",
        cache_dir="./models"
    )
except Exception as e:
    print(f"Failed to initialize QA pipeline: {e}")
    qa_pipeline = None


def ask_richard_offline(question: str, context: str) -> str:
    """
    Answers a question using a local transformer QA model.

    Args:
        question (str): The question to ask.
        context (str): The context to search the answer in.

    Returns:
        str: The predicted answer or error message.
    """
    if not qa_pipeline:
        return "Offline QA model is not available."

    try:
        result = qa_pipeline(question=question, context=context)
        return result.get("answer", "No answer found.")
    except Exception as e:
        print(f"[Offline QA Error] {e}")
        return "I'm sorry, I couldn't process your question offline."
