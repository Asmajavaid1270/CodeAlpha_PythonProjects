import random

def hangman():
    words = ["python", "developer", "hangman", "computer", "algorithm"]
    word = random.choice(words)
    guessed = set()
    attempts = 6

    print("\n🎮 Welcome to Hangman Game!")
    print(f"You have {attempts} wrong attempts. Good luck!")

    while attempts > 0:
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print("\nWord:", display)

        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed:
            print("⚠ You already guessed that letter!")
            continue

        guessed.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        else:
            print("✅ Good guess!")

        if all(letter in guessed for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"\n😢 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()