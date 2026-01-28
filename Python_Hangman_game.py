import random
words = ["Pumpkin", "taxidermy", "Pidgeon", "abruptly","absurd","abyss","affix","askew","avenue","awkward",
"axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard",
"boggle","bookworm","boxcar","boxful","buckaroo","buffalo","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazzy",
"jelly","jigsaw","jinx","jiujitsu"]
word = random.choice(words).lower()
print("Welcome to Hangman!")
guessed_letters = []
lives = 6

while lives > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Enter ONE letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        lives -= 1
        print("Wrong! Lives left:", lives)

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("🎉 You win!")
        break