import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training dataset
data = {
    "message": [
        "You won a free gift",
        "Click here to claim your prize",
        "Urgent verify your account",
        "You won a lottery",
        "Claim your cash reward now",
        "Your account is suspended",
        "Congratulations you are selected",
        "Update your bank password",
        "Hello how are you",
        "See you tomorrow",
        "Class starts at 9 AM",
        "Thank you for your help",
        "Please attend the meeting",
        "I will call you later",
        "Have a wonderful day",
        "Happy birthday to you"
    ],
    "label": [
        "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing", "phishing",
        "safe", "safe", "safe", "safe",
        "safe", "safe", "safe", "safe"
    ]
}

df = pd.DataFrame(data)

# Train ML model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])

model = MultinomialNB()
model.fit(X, df["label"])

# Suspicious keywords
suspicious_words = [
    "winner",
    "free gift",
    "click here",
    "claim your prize",
    "urgent",
    "password",
    "verify account",
    "lottery"
]

# User input
message = input("Enter a message to check: ")

# Keyword detection
found_words = []

for word in suspicious_words:
    if word in message.lower():
        found_words.append(word)

# ML prediction
message_vector = vectorizer.transform([message])
prediction = model.predict(message_vector)[0]

# Final report
print("\n--- PHISHING DETECTION REPORT ---")
print("ML Prediction:", prediction)
print("Suspicious Keywords:", found_words)

if prediction == "phishing" or found_words:
    print("Risk Level: HIGH")
    print("Warning: Potential phishing message!")
else:
    print("Risk Level: LOW")
    print("Message appears safe.")

print("Detection completed!")