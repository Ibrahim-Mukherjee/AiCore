import random

# Step 1: Create a list containing the names of your 5 favorite fruits
# Step 2: Assign this list to a variable called word_list
word_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Step 3: Use the random.choice method and pass the word_list variable into the choice method
# Step 4: Assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()
    # Step 3: Move the code that checks if the guess is in the word into this function block
    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Move the code that checks if the input is a valid guess into this function block
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Outside the function, call the ask_for_input function to test your code
ask_for_input()