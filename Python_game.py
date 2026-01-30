import random

print("welcom to Hangman")

words = ["switch", "possession", "straw", "bathtub", "glance", "tick", "like", "dramatic", "even", "low", "dare", "pioneer", "sugar", "critical", "choke", "ladder", "surprise", "desire", "illness", "magnitude", "train", "firm", "robot", "banner", "omission"]
word = random.choice(words)

guesses = ''
turns = 6
print("DEBUG → turns:", turns)
print("DEBUG → guesses:", guesses)

hangman_stages = [
    """
     ------
     |    |
     |
     |
     |

    """,
    """
     ------
     |    |
     |    O
     |
     |

    """,
    """
     ------
     |    |
     |    O
     |    |
     |

    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
    ------
    """
]

while turns > 0:
    print(hangman_stages[6 - turns])

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1

    print()

    if failed == 0:
        print("You Win")
        print("The word is:", word)
        break

    guess = input("guess a character: ").lower()

    if guess == "":
        print("No input detected.")
        continue

    if len(guess) != 1:
        print("Please enter exactly ONE letter.")
        continue

    if not guess.isalpha():
        print("Letters only.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

        if turns == 0:
            print(hangman_stages[6])
            print("You Lose")
            print("The word is:", word)


