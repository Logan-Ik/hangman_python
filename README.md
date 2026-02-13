Hangman Game (Python)

A command-line Hangman game implemented in Python. Players guess letters to reveal a randomly chosen word before running out of attempts. This project is perfect for beginners learning Python basics, loops, conditionals, and string manipulation.

Features

Randomly selects a word from a predefined list
Tracks player guesses and prevents repeated guesses
Displays the Hangman figure as the player makes wrong guesses
Input validation: only accepts **single alphabetic letters**
Win/lose detection with messages and the correct word displayed

How to Play

1. Run the Python script:

```bash
python hangman.py
```

2. The game displays underscores (`_`) for each letter in the word.

3. Type a single letter to guess:

If the letter is in the word, it is revealed in its correct position
If the letter is not in the word, you lose one turn and a part of the Hangman is drawn

4. The game ends when:

You guess all letters correctly → You Win
You run out of 6 guesses → You Lose, and the correct word is shown

---

Example Gameplay

```
DEBUG → turns: 6
DEBUG → guesses: 

_ _ _ _ _ _ 

guess a character: a
Wrong
You have 5 more guesses
```

As you make wrong guesses, the Hangman figure is drawn progressively:

```
 ------ 
 |    |
 |    O
 |   /|\
 |   / \
------
```

Code Highlights

 `words` – a list of possible words
`turns` – number of allowed wrong guesses (6)
`guesses` – stores letters guessed so far
`hangman_stages` – ASCII art for the hangman figure
 Input validation for empty input, multiple letters, non-alphabetic input, or repeated guesses



Requirements

Python 3.x

No external libraries are required.

How to Extend

Load words from an external file for more variety
Add difficulty levels by changing number of guesses or word length
Implement scoring based on remaining turns


