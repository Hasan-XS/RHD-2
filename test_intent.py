import pickle

# Load model
with open('models/intent_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

while True:
    sentence = input("You: ")
    if sentence.lower() == "exit":
        break
    pred = model.predict([sentence])[0]
    tag = le.inverse_transform([pred])[0]
    print(f"Predicted intent tag: {tag}")

