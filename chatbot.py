def chatbot():
    print("\n🤖 Chatbot is online! Type 'bye' to exit.")
    responses = {
        "hello": "Hi there! 😊",
        "how are you": "I'm fine, thanks! How about you?",
        "your name": "I'm CodeAlphaBot 🤖",
        "thanks": "You're welcome! 😄"
    }

    while True:
        user = input("You: ").lower().strip()
        if user == "bye":
            print("Bot: Goodbye! 👋")
            break
        print("Bot:", responses.get(user, "Sorry, I don't understand 😅"))

if __name__ == "__main__":
    chatbot()