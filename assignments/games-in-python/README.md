
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman (word-guessing) game to practice string manipulation, loops, conditionals, and basic user input/output in Python.

## 📝 Tasks

### 🛠️ Game Implementation

#### Description
Implement a command-line Hangman game where the program randomly selects a secret word and the player guesses letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (or a provided word file).
- Prompt the player to guess single letters and show current progress using underscores and revealed letters (e.g. `_ a _ _ m a n`).
- Track and display incorrect guesses and remaining attempts.
- Prevent repeated guesses from counting as new incorrect attempts and notify the player if a letter was already tried.
- End the game with a clear win or lose message and reveal the secret word on loss.
- Include a short `starter-code.py` that initializes the word list and shows how to accept player input.

## 🔎 Example Input / Output

Example interaction (user input shown after `>`):

```
Welcome to Hangman!
_ _ _ _ _ _ _
Guesses left: 6
Wrong guesses: 
> a
Correct! Current word: _ a _ _ _ a _
Guesses left: 6
Wrong guesses: 
> z
Wrong guess. Guesses left: 5
Wrong guesses: z
```

## 🧾 Starter files

- `starter-code.py` — Basic scaffold (word list loader, input loop) placed in the same folder.

## ✅ Evaluation checklist

- Game runs from the command line and accepts input until the game ends.
- Reveals letters correctly and handles repeated guesses.
- Provides clear win/lose messaging and does not crash on unexpected input.

## 💡 Hints

- Use `random.choice()` for selecting a word.
- Use a `set` to track guessed letters.
- Update the displayed word by iterating over characters and revealing guessed letters.

**Skills practiced:** String manipulation, loops, conditionals, user I/O, basic program state management
