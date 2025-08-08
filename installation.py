import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import datetime
import random

# Setup
lemmatizer = WordNetLemmatizer()

# Sample jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the math book sad? Because it had too many problems.",
]

# Intent keywords
intents = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how", "are", "you"],
    "name": ["name"],
    "bye": ["bye", "exit", "quit"],
    "help": ["help", "commands"],
    "time": ["time", "clock"],
    "date": ["date", "day"],
    "joke": ["joke", "funny"],
    "weather": ["weather"],
    "thanks": ["thank", "thanks"],
}

# Intent responses
responses = {
    "greeting": "Hello there! 😊",
    "how_are_you": "I'm doing great! Thanks for asking. How can I help you?",
    "name": "I'm a simple chatbot created in Python with a touch of NLTK!",
    "bye": "Goodbye! 👋",
    "help": "You can say hi, ask the time, date, tell a joke, or say bye!",
    "time": lambda: f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}.",
    "date": lambda: f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}.",
    "joke": lambda: random.choice(jokes),
    "weather": "I'm offline, so I can't fetch live weather. But I hope it's sunny! ☀️",
    "thanks": "You're welcome! 😊"
}

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized

def detect_intent(lemmatized_tokens):
    for intent, keywords in intents.items():
        if any(word in lemmatized_tokens for word in keywords):
            return intent
    return "unknown"

def chatbot_response(user_input):
    tokens = preprocess_input(user_input)
    intent = detect_intent(tokens)

    if intent in responses:
        response = responses[intent]
        return response() if callable(response) else response
    else:
        return "I'm not sure how to respond to that. Try asking something else."

# Chat loop
print("🤖 NLTK Chatbot (Offline) — Type 'exit' to quit\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot:", responses["bye"])
        break
    print("Chatbot:", chatbot_response(user_input))



