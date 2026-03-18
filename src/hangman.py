import random
from typing import List, Set

class HangmanGame:
    def __init__(self):
        self.WORD_LIST: List[str] = ["python", "developer", "algorithm", "interface", "database"]
        self.MAX_ATTEMPTS: int = 6
        self.current_word: str = ""
        self.guessed_letters: Set[str] = set()
        self.attempts_left: int = 0

    def _select_word(self) -> str:
        return random.choice(self.WORD_LIST).lower()

    def _display_word(self) -> str:
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.current_word])

    def _handle_guess(self, guess: str) -> bool:
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input! Please enter a single letter.")
            return False
        if guess in self.guessed_letters:
            print("⚠️ You already guessed that letter!")
            return False
        self.guessed_letters.add(guess)
        return True

    def play(self):
        self.current_word = self._select_word()
        self.attempts_left = self.MAX_ATTEMPTS
        self.guessed_letters = set()
        print("\n🎮 === HANGMAN GAME STARTED === 🎮")
        
        while self.attempts_left > 0:
            print(f"\nWord: {self._display_word()}")
            print(f"❤️ Attempts Left: {self.attempts_left}")
            guess = input("👉 Enter a letter: ").lower()
            if not self._handle_guess(guess):
                continue
            if guess not in self.current_word:
                self.attempts_left -= 1
                print("❌ Wrong guess!")
            else:
                print("✅ Correct guess!")
            if all(letter in self.guessed_letters for letter in self.current_word):
                print(f"\n🏆 Congratulations! You won! The word was: {self.current_word}")
                break
        else:
            print(f"\n💀 Game Over! The word was: {self.current_word}")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()