import spacy

class NLPProcessor:
    def __init__(self, model_name: str = "en_core_web_sm"):
        try:
            self.nlp = spacy.load(model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to load SpaCy model '{model_name}': {e}")

    def extract_keywords(self, text: str) -> str:
        """
        Extracts meaningful keywords (nouns, verbs, adjectives, adverbs) from a given text.
        
        :param text: Input sentence or paragraph
        :return: String containing filtered keywords
        """
        try:
            doc = self.nlp(text)
            keywords = [token.text for token in doc if token.pos_ in {"NOUN", "VERB", "ADJ", "ADV"}]
            return " ".join(keywords).strip()
        except Exception as e:
            print(f"[NLP ERROR] Failed to process text: {e}")
            return ""
