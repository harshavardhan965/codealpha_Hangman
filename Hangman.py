import random

# Predefined list of words
word_list = ['apple', 'table', 'zebra', 'robot', 'grape']

# Select a random word
word_to_guess = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display setup
display_word = ['_'] * len(word_to_guess)

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("Word:", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetical character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!\n")
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[idx] = guess
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong_guesses - wrong_guesses} guesses left.\n")

# Game result
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game Over! The word was:", word_to_guess)
