
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from datetime import datetime

import csv
from io import StringIO
from flask import Response
import os
app = Flask(__name__)

# Training dataset
data = {
    "message": [
        "You won a free gift",
        "Click here to claim your prize",
        "Urgent verify your account",
        "You won a lottery",
        "Claim your cash reward",
        "Your account is suspended",
        "Hello how are you",
        "See you tomorrow",
        "Class starts at 9 AM",
        "Thank you for your help",
        "Happy birthday wishing you happiness",
"Have a wonderful day",
"Thank you for your support",
"Congratulations on your success",
"Hope you have a great weekend",
"Good morning have a nice day",
"See you at college tomorrow",
"Best wishes for your future"
    ],
    "label": [
        "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing",
        "safe", "safe", "safe", "safe","safe","Safe","safe","safe","safe","safe","safe","safe"
    ]
}

df = pd.DataFrame(data)

# Machine Learning model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])

model = MultinomialNB()
model.fit(X, df["label"])

# Suspicious keywords
suspicious_keywords = [
    "free gift",
    "click here",
    "claim your prize",
    "urgent",
    "password",
    "verify your account",
    "lottery",
    "cash reward",
    "account suspended",
    "account is suspended"
]

scan_history = []

# Website route
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        if request.form.get("action") == "clear":
            scan_history.clear()
            return redirect(url_for("home"))

        message = request.form.get("message", "").strip()

        if message:

            # Convert message into numerical format
            message_vector = vectorizer.transform([message])

            # Predict phishing or safe
            prediction = model.predict(message_vector)[0]

            # Find suspicious keywords
            found_keywords = []

            for keyword in suspicious_keywords:
                if keyword in message.lower():
                    found_keywords.append(keyword)

            # Risk level calculation
            if len(found_keywords) >= 3:
                risk = "HIGH"
            elif len(found_keywords) >= 1:
                risk = "MEDIUM"
            else:
                risk = "LOW"

            # Store scan history
            scan_history.append({
                "message": message,
                "prediction": prediction,
                "risk": risk,
                "date":datetime.now().strftime("%d-%m-%Y"),
                "time":datetime.now().strftime("%I:%M:%S %p")
            })

            # Display prediction result
            if prediction == "phishing":
                result = "WARNING! Potential Phishing Message"
            else:
                result = "Message appears Safe"

            result += " | Risk Level: " + risk

            if found_keywords:
                result += " | Suspicious Keywords: " + ", ".join(found_keywords)

            # Explain suspicious keywords
            explanations = []

            for keyword in found_keywords:

                if keyword in ["urgent", "click here"]:
                    explanations.append(
                        "Urgent or suspicious action requested"
                    )

                elif keyword in [
                    "free gift", "lottery",
                    "cash reward", "claim your prize"
                ]:
                    explanations.append(
                        "Unusual reward or prize offer detected"
                    )

                elif keyword in ["password", "verify your account"]:
                    explanations.append(
                        "Account verification or password request detected"
                    )

                elif keyword in [
                    "account suspended", "account is suspended"
                ]:
                    explanations.append(
                        "Account suspension warning detected"
                    )

            if explanations:
                result += " | Why Suspicious: " + "; ".join(explanations)

    # Dashboard statistics
    total_scanned = len(scan_history)

    phishing_count = sum(
        1 for scan in scan_history
        if scan["prediction"] == "phishing"
    )

    safe_count = sum(
        1 for scan in scan_history
        if scan["prediction"] == "safe"
    )
    phishing_percentage = (
    (phishing_count / total_scanned) * 100
    if total_scanned > 0 else 0
)

    # Display dashboard
    return render_template(
        "index.html",
        result=result,
        scan_history=scan_history,
        total_scanned=total_scanned,
        phishing_count=phishing_count,
        safe_count=safe_count,
        phishing_percentage=round(phishing_percentage,2)
    )
@app.route("/export")
def export_history():
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Message", "Prediction", "Risk", "Date", "Time"])

    for scan in scan_history:
        writer.writerow([
            scan["message"],
            scan["prediction"],
            scan["risk"],
            scan["date"],
            scan["time"]
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=scan_history.csv"}
    )

# Run Flask application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
