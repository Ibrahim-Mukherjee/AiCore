import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters = len(set(self.word) - set(self.word_guessed))
            if '_' not in self.word_guessed:
                print("Congratulations! You've guessed the word correctly.")
                print(f"The word was: {self.word}")
                return True
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("You've run out of lives. Game over!")
                print(f"The word was: {self.word}")
                return True
        return False

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                if self.check_guess(guess):
                    break
                print(f"Current word: {' '.join(self.word_guessed)}")
                print(f"Lives left: {self.num_lives}")
                print(f"Guesses so far: {', '.join(self.list_of_guesses)}")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# Step 2: Call your play_game function to play your game
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
play_game(word_list)