import datetime
import random

print("🤖 Simple Chatbot (Offline, No AI) — Type 'exit' to quit\n")

# Sample jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the math book sad? Because it had too many problems.",
]

# Predefined responses using keyword matching
def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 😊"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. How can I help you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created in Python!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋"
    elif "help" in user_input:
        return "You can say hi, ask my name, ask the time or date, or ask for a joke!"
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif "date" in user_input or "day" in user_input:
        today = datetime.datetime.now()
        return f"Today is {today.strftime('%A, %B %d, %Y')}."
    elif "joke" in user_input:
        return random.choice(jokes)
    elif "weather" in user_input:
        return "I'm offline, so I can't fetch live weather. But I hope it's sunny where you are! ☀️"
    elif "thank" in user_input:
        return "You're welcome! 😊"
    else:
        return "I'm not sure how to respond to that. Try asking something else."

# Chat loop
while True:
    user_message = input("You: ")
    response = simple_chatbot(user_message)
    print("Chatbot:", response)
    if user_message.lower() in ["exit", "quit", "bye"]:
        break
