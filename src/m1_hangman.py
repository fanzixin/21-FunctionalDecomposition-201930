"""
Hangman.

Authors: Zixin Fan and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random

def main():
    [mininum_length, N] = Set_Difficulty()
    secret_word = Pick_a_word(mininum_length)
    print(secret_word)

    Get_a_guess()


def Set_Difficulty():
    print('-------------------------------------------------------------')
    print('Set Difficulty')
    print('-------------------------------------------------------------')

    minimun_length = int(input("What's the MININUM length do you want for the secret word? \n     L = "))
    print()
    print("You set the DIFFICULTY of the game by setting the number of \n"
          "UNSUCCESSFUL choices you can make before you LOSE the game. \n"
          "The traditional form of Hangman sets this number to 5.")
    unsuccessful_choices = int(input('How many unsuccessful choices do you want to allow yourself? \n     N = '))
    print()

    return minimun_length, unsuccessful_choices


def Pick_a_word(minimun_length):
    print('-------------------------------------------------------------')
    print("Let's start the game!")
    print('-------------------------------------------------------------')

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

    while True:
        r = random.randrange(0, len(words))
        if len(words[r]) <= minimun_length:
            break

    L = len(words[r])

    print('Here is what you currently know about the secret word:')
    print('-' * L)
    print()

    return words[r]

def Get_a_guess():
    letter = str(input('What letter do you want to try? \n     letter = '))

main()

####### Do NOT attempt this assignment before class! #######

