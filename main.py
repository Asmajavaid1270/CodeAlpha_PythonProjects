from src.hangman import HangmanGame
from src.stock_tracker import PortfolioManager
from src.chatbot import RuleBasedBot

def display_menu():
    print("\n" + "="*40)
    print("💻 CODEALPHA PYTHON PROJECTS SUITE")
    print("="*40)
    print("1. 🎮 Play Hangman")
    print("2. 📈 Stock Portfolio Tracker")
    print("3. 🤖 Chat with Bot")
    print("4. 🚪 Exit")
    print("="*40)

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            HangmanGame().play()
        elif choice == "2":
            PortfolioManager().run()
        elif choice == "3":
            RuleBasedBot().run()
        elif choice == "4":
            print("👋 Thank you for using CodeAlpha Projects!")
            break
        else:
            print("❌ Invalid selection. Please try again.")

if __name__ == "__main__":
    main()