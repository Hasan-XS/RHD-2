import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

class IntentClassifier:
    def __init__(self, model_path="intents/intent_classifier.joblib", dataset_path="intents/intents.csv"):
        self.model_path = model_path
        self.dataset_path = dataset_path
        self.model = None

        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)

    def train(self):
        df = pd.read_csv(self.dataset_path)
        texts = df["text"]
        labels = df["intent_name"]

        X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression(max_iter=1000))
        ])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        print("Intent Classifier Report:")
        print(classification_report(y_test, y_pred))

        joblib.dump(pipeline, self.model_path)
        self.model = pipeline

    def predict(self, text):
        if self.model is None:
            raise Exception("Model not loaded. Please train the model first.")
        return self.model.predict([text])[0]
