import random
import time

name = input("What is your name?: ")
print("Welcome to hangman " + name + "! Good luck!")
time.sleep(1)
print("You can choose each letter more than once. Good luck!")
time.sleep(2)
print("The game begins now...\n")
time.sleep(2)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_again
    global score
    secret_word = ["rose", "tulip", "daisy", "orchid", "daffodil", "sunflower", "iris", "lily", "lavender"]
    word = random.choice(secret_word)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_again = ""


games_won = 0
games_lost = 0


def again_play():
    global play_again
    play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    while play_again not in ["1", "2"]:
        play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    if play_again == "1":
        main()
        hangman()
    elif play_again == "2":
        score()
        time.sleep(2)
        exit()




def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_again
    global score

    limit = 5
    guess = input("The word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Enter only one letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("You have already guessed this letter. Try another letter\n")

    else:
        count += 1

        if count == 1:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 2:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 3:
            print("Wrong choice. \n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 4:
            print("Wrong choice.\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
        elif count == 5:
            print("Wrong choice. You are hanged\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            again_play()

    if word == '*' * length:
        print("Congrats! You have guessed it successfully...")
        again_play()

    elif count != limit:
        hangman()


main()


def score():
    print(" ")
    print("  Score")
    print("  -----")
    print("  Won: " + str(games_won) + "    Lost: " + str(games_lost))

hangman()
main()

leaderboard1 = open('leaderboardFile1.txt', 'a')
leaderboard1.write(name + str(games_won))
leaderboard1.close()

hangman()
