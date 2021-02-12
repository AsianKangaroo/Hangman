import random
import re

print("Welcome to Hangman!")
print("Guesses are limited to single, lower-case letters")
print("because of important classified reasons")
print("(I'm not lazy I swear)")
print("P.S. The words are completely random")
print("Good luck, have fun >:)")
print()

word_list = [
    "father", "airport", "analysis", "development", "celebration", "oven",
    "finding", "customer", "control", "procedure", "agenda", "assignment",
    "cartridge,", "cod", "elver", "footrest", "giggle", "left", "urmom",
    "chromolithograph", "commuter", "garter", "graph", "running", "nut",
    "schedule", "exwife", "stopsign", "thickness"
]
rand_num = random.randrange(0, 30)
word = []
for letter in word_list[rand_num]:
    word += letter

animal_list = [
    "ʕ •ᴥ•ʔ", "εїз", "ฅ^•ﻌ•^ฅ", "(ᵔᴥᵔ)", "くコ:彡", "ʕ·ᴥ·ʔ", "=✪ ᆺ ✪=",
    "ʕ •̀ ω •́ ʔ", ">:3 \nRAWR I AM LION"
]
rand_num_2 = random.randrange(0, 10)
displayed_word = []
for i in range(len(word)):
    displayed_word.append("-")
mistakes = []
lives = 6
epic_gamin = True
wins = 0
losses = 0

def list_to_string(l):
    string = ""
    for element in l:
        string += element
    return string

word_constant = list_to_string(word.copy())

def draw_hanged_dude():
    if lives == 6:
        print(" _____")
        print("|")
        print("|")
        print("|")
        print("____")
    elif lives == 5:
        print(" _____")
        print("|    o")
        print("|")
        print("|")
        print("____")
    elif lives == 4:
        print(" _____")
        print("|    o")
        print("|    |")
        print("|")
        print("____")
    elif lives == 3:
        print(" _____")
        print("|    o")
        print("|   /|")
        print("|")
        print("____")
    elif lives == 2:
        print(" _____")
        print("|    o")
        print("|   /|\\")
        print("|")
        print("____")
    elif lives == 1:
        print(" _____")
        print("|    o")
        print("|   /|\\")
        print("|   /")
        print("____")
    elif lives == 0:
        print(" _____")
        print("|    o")
        print("|   /|\\")
        print("|   / \\")
        print("____")

def game_state():
    print(str(lives) + " Lives Left")
    draw_hanged_dude()
    print("Mistakes: " + list_to_string(mistakes))
    print()
    print(list_to_string(displayed_word))
    print("___________________________________")
    print()

while epic_gamin:
    while lives > 0:
        game_state()
        guess = input("Guess a letter: ")
        while guess in mistakes or guess in displayed_word or len(
                guess) != 1 or not re.match("^[a-z]*$", guess):
            guess = input("Your input is garbage human, try again: ")
        if guess in word:
            for char in word:
                if char == guess:
                    displayed_word[word.index(char)] = char
                    word[word.index(char)] = "-"
        else:
            mistakes.append(guess)
            mistakes.append(", ")
            lives -= 1
        if lives == 0:
            game_state()
            print("The word was: " + word_constant)
            print("You lost... D:")
            print()
            print("R.I.P. digital construct of a man whose sole purpose")
            print("for existence was to serve as a visual ")
            print("representation of the amount of lives you have")
            losses += 1
            print()
            print("Wins: " + str(wins))
            print("Losses: " + str(losses))
            print()
            play_again = input("Play Again? (y/n): ")
            while play_again != "n" or play_again != "y":
                if play_again == "n" or play_again == "y":
                    break
                play_again = input(
                    "Your input is garbage human, try again (y/n): ")
            if play_again == "y":
                rand_num = random.randrange(0, 30)
                word = []
                for letter in word_list[rand_num]:
                    word += letter
                word_constant = list_to_string(word.copy())
                displayed_word = []
                for i in range(len(word)):
                    displayed_word.append("-")
                mistakes = []
                lives = 6
                break
            elif play_again == "n":
                epic_gamin = False
                break
        if "-" not in displayed_word:
            game_state()
            print("The word was: " + word_constant)
            print("You win! Callooh! Callay!")
            print("Here, have some dopamine:")
            print(animal_list[rand_num_2])
            wins += 1
            print("Wins: " + str(wins))
            print("Losses: " + str(losses))
            play_again = input("Play Again? (y/n): ")
            while play_again != "n" or play_again != "y":
                if play_again == "n" or play_again == "y":
                    break
                play_again = input(
                    "Your input is garbage human, try again (y/n): ")
            if play_again == "y":
                rand_num = random.randrange(0, 30)
                word = []
                for letter in word_list[rand_num]:
                    word += letter
                word_constant = list_to_string(word.copy())
                displayed_word = []
                for i in range(len(word)):
                    displayed_word.append("-")
                mistakes = []
                lives = 6
                break
            elif play_again == "n":
                print("bye bye!")
                exit()
