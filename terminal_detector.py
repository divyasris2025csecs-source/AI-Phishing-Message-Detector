suspicious_keywords = [
    "free gift",
    "click here",
    "claim your prize",
    "urgent",
    "password",
    "verify your account",
    "lottery",
    "cash reward",
    "account suspended"
]

print("================================")
print("     AI PHISHING DETECTOR")
print("================================")

message = input("\nEnter your message: ")

found_keywords = []

for keyword in suspicious_keywords:
    if keyword in message.lower():
        found_keywords.append(keyword)

if found_keywords:
    print("\nWARNING! Potential Phishing Message")
    print("Suspicious keywords found:", ", ".join(found_keywords))
else:
    print("\nNo suspicious keywords detected.")

print("\nNote: This is a basic keyword check, not a guarantee that a message is safe.")