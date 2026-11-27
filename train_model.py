
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Dataset
data = {
    "message": [
        "You won a free gift",
        "Click here to claim your prize",
        "Urgent verify your account",
        "You won a lottery",
        "Claim your cash reward now",
        "Your account is suspended verify now",
        "Congratulations you are selected",
        "Update your bank password immediately",
        "You received a free coupon",
        "Click to win exciting prizes",
        "Hello how are you",
        "See you tomorrow",
        "Class starts at 9 AM",
        "Thank you for your help",
        "Please attend the meeting",
        "I will call you later",
        "Your assignment is ready",
        "Have a wonderful day",
        "The meeting starts at noon",
        "Happy birthday to you"
    ],
    "label": [
        "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing",
        "safe", "safe", "safe", "safe", "safe",
        "safe", "safe", "safe", "safe", "safe"
    ]
}

df = pd.DataFrame(data)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["message"],
    df["label"],
    test_size=0.25,
    random_state=42,
    stratify=df["label"]
)

# Convert text into numbers
vectorizer = CountVectorizer()

X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vector, y_train)

# Predict test messages
predictions = model.predict(X_test_vector)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("--- MODEL ACCURACY REPORT ---")
print("Total test messages:", len(y_test))
print("Correct predictions:", sum(predictions == y_test))
print("Model accuracy:", round(accuracy * 100, 2), "%")
# Confusion Matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["phishing", "safe"]
)

print("\n--- CONFUSION MATRIX ---")
print(cm)

# Classification Report
print("\n--- CLASSIFICATION REPORT ---")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))