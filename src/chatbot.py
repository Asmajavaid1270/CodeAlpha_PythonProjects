from typing import Dict

class RuleBasedBot:
    def __init__(self):
        self.responses: Dict[str, str] = {
            "hello": "Hi there! 😊 How can I help you today?",
            "hi": "Hello! 👋 Welcome to CodeAlpha Bot.",
            "how are you": "I'm just a bot, but I'm functioning well! 🤖",
            "name": "I am CodeAlpha Assistant Bot.",
            "help": "I can answer basic questions. Try 'hello', 'name', or 'bye'.",
            "bye": "Goodbye! 👋 Have a great day!"
        }
        self.is_active: bool = True

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()
        for key, value in self.responses.items():
            if key in user_input:
                return value
        return "😅 I'm not sure I understand. Try typing 'help'."

    def run(self):
        print("\n🤖 === CODEALPHA CHATBOT === 🤖")
        print("Type 'bye' to exit.\n")
        while self.is_active:
            try:
                user_input = input("👤 You: ")
                if not user_input.strip():
                    continue
                response = self.get_response(user_input)
                print(f"🤖 Bot: {response}")
                if "bye" in user_input.lower():
                    self.is_active = False
            except KeyboardInterrupt:
                print("\n🛑 Chat interrupted.")
                break

if __name__ == "__main__":
    bot = RuleBasedBot()
    bot.run()