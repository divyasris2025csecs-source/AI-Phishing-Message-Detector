
message = input("Enter your message: ")

suspicious_words = [
    "winner",
    "free gift",
    "click here",
    "claim your prize",
    "urgent",
    "password",
    "verify your account"
]

found_words = []

for word in suspicious_words:
    if word.lower() in message.lower():
        found_words.append(word)

count = len(found_words)

print("\n--- Phishing Detection Report ---")

if count == 0:
    print("Risk Level: LOW")
    print("No suspicious keywords found.")
elif count <= 2:
    print("Risk Level: MEDIUM")
    print("Suspicious message detected!")
else:
    print("Risk Level: HIGH")
    print("Highly suspicious message detected!")

print("Suspicious keyword count:", count)
print("Detected words:", found_words)
