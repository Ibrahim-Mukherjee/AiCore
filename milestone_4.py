import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess.lower())
                # Check if the game is over
                if self.num_letters == 0:
                    print("Congratulations! You've guessed the word correctly.")
                    break
                if self.num_lives == 0:
                    print("You've run out of lives. Game over!")
                    break
                print(f"Current word: {' '.join(self.word_guessed)}")
                print(f"Lives left: {self.num_lives}")
                print(f"Guesses so far: {', '.join(self.list_of_guesses)}")
                # If the game is not over, continue asking for input
                continue

def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word.lower():
        print(f"Good guess! {guess} is in the word.")
        for index, letter in enumerate(self.word):
            if letter.lower() == guess:
                self.word_guessed[index] = letter
        self.num_letters -= 1
        # Check if the game is won
        if '_' not in self.word_guessed:
            print("Congratulations! You've guessed the word correctly.")
            print(f"The word was: {self.word}")
    else:
        # Step 1: Create an else statement
        # Step 2: Within the else block:
        self.num_lives -= 1  # Reduce num_lives by 1
        print(f"Sorry, {guess} is not in the word.")  # Print a message saying "Sorry, {letter} is not in the word."
        print(f"You have {self.num_lives} lives left.")  # Print another message saying "You have {num_lives} lives left."
        # Check if the game is over
        if self.num_lives == 0:
            print("You've run out of lives. Game over!")
            print(f"The word was: {self.word}")

# Example usage
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
game = Hangman(word_list)
game.ask_for_input()