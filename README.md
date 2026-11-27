# 🔐 AI-Powered Phishing & Scam Message Detector

An educational AI and Cybersecurity project that explores how Machine Learning can help identify potentially suspicious phishing and scam messages.

## 🚀 About the Project

The AI-Powered Phishing & Scam Message Detector is a beginner-level web application developed using Python and Machine Learning.

It analyzes text messages and classifies them as potentially phishing or safe using a basic Machine Learning model.

The project also identifies suspicious keywords and displays a risk level to help users understand potential warning signs.

## ✨ Key Features

- **Message Classification:** Classifies messages as Phishing or Safe.
- **Suspicious Keyword Detection:** Identifies potentially suspicious words and phrases.
- **Risk Level Indicator:** Displays Low, Medium, or High risk levels.
- **Scan History:** Maintains a record of scanned messages with date and time.
- **Dashboard Statistics:** Displays total scanned, phishing and safe message counts.
- **CSV Export:** Allows users to download scan history.
- **Clear History:** Allows users to clear previous scan records.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Machine Learning | Message classification |
| Scikit-learn | Model training and prediction |
| Flask | Web application framework |
| HTML | Webpage structure |
| CSS | User interface styling |

## 📂 Project Structure

```text
AI-Phishing-Message-Detector/
│
├── app.py
├── phishing_detector.py
├── train_model.py
├── final_detector.py
├── terminal_detector.py
│
├── templates/
│   └── index.html
│
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/divyasri2025csecs-source/AI-Phishing-Message-Detector.git
```

**2. Open the project folder**

```bash
cd AI-Phishing-Message-Detector
```

**3. Install the required libraries**

```bash
pip install flask scikit-learn pandas
```

**4. Run the Flask application**

```bash
python app.py
```

**5. Open the application**

Visit:

```text
http://127.0.0.1:5000
```

## 🧠 Machine Learning Approach

The project uses:

- CountVectorizer for converting text into numerical features.
- Multinomial Naive Bayes for basic text classification.

The application also uses keyword matching to identify suspicious terms and indicate a simple risk level.

## 📚 Learning Outcomes

Through this project, I explored:

- Python programming.
- Basic Machine Learning concepts.
- Text classification.
- Flask application development.
- Frontend and backend integration.
- Testing and debugging.
- Basic cybersecurity awareness.

## ⚠️ Disclaimer

This project is developed for educational and learning purposes.

It is a basic prototype trained and tested using a small sample dataset. Its predictions are not guaranteed to be accurate and should not be used as the sole basis for real-world security decisions. A message classified as safe may still be malicious.

## 👩‍💻 Author

**Divya Sri S**

B.E. Cybersecurity Student

## 🌱 Future Improvements

- Expand and improve the training dataset.
- Evaluate the model using larger and more diverse datasets.
- Improve classification performance.
- Explore additional phishing detection techniques.

---

⭐ Thank you for visiting my project repository!

**Learn. Build. Test. Improve.**
