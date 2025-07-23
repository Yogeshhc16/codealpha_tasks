import random
# 1. Predefined list of words
word_list = ["apple", "house", "train", "plant", "candy", "priya", "vikas"]
# 2. Select a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
max_incorrect = 6
incorrect_guesses = 0
print("Welcome to Hangman!")
print("_ " * len(secret_word))  # Display blanks for each letter
# 3. Game loop
while incorrect_guesses < max_incorrect:
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess. You have {max_incorrect - incorrect_guesses} tries left.")
    # Show current progress
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())
    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break
# If the player used all attempts and didn't guess the word
if incorrect_guesses == max_incorrect:
    print(f"Game over! The word was: {secret_word}")
