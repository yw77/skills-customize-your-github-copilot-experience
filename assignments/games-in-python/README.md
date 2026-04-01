
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Set Up Word Selection

#### Description
Create a list of words and use Python's `random` module to randomly select a hidden word for each round of the game.

#### Requirements
Completed program should:

- Define a list of at least 5 words to choose from
- Randomly select one word at the start of each game
- Keep the selected word hidden from the player

### 🛠️	Implement Game Loop and Guessing

#### Description
Build the core game loop that accepts letter guesses from the player, tracks progress, and displays the current state of the word.

#### Requirements
Completed program should:

- Accept single letter guesses from user input
- Display current progress in `_ _ _` format, revealing correctly guessed letters
- Track and display the number of incorrect guesses remaining
- Prevent duplicate guesses from counting against the player

### 🛠️	Handle Win and Lose Conditions

#### Description
Add logic to end the game when the player has either guessed the full word or exhausted all allowed attempts.

#### Requirements
Completed program should:

- End the game when all letters in the word have been guessed
- End the game when the player runs out of attempts
- Display a win message with the completed word on success
- Display a lose message revealing the hidden word on failure
