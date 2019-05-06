"""
Hangman.

Authors: Zixin Fan and YOUR_PARTNERS_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan

import random

def main():
    [mininum_length, N] = Set_Difficulty()
    secret_word = Pick_a_word(mininum_length)

    Play_the_game(secret_word, N)

    Play_again()


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

    return words[r]


def Get_a_guess():
    letter = str(input('What letter do you want to try? \n     letter = '))
    print()
    return letter


def Check_if_reinput_same_letter(letter, input_letters):
    i = 0

    while True:
        if i == len(input_letters):
            break
        if input_letters[i] == letter:
            print('Reminder! You have already input the letter', letter,
                  '\nPlease input another letter.')
            return True
        i = i + 1

    return False


def Get_an_effective_guess(input_letters):
    while True:
        letter = Get_a_guess()
        reinput_or_not = Check_if_reinput_same_letter(letter, input_letters)
        if reinput_or_not == False:
            break

    return letter


def Check_the_letter(secret_word, letter):
    position = []

    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            position = position + [i]
            # When letter appears more than once in the secret_word, position has more than one element!!!

    if len(position) != 0:
        return True, position
    else:
        return False, position


def Report_each_guess(answer, letter, trails_left):
    if answer == False:
        print('Sorry! There are no', letter, 'letters in the secret word. \n'
              'You have', trails_left, 'unsuccessful guess(es) left before you \n'
              'LOSE the game!')
    else:
        print('Good guess! You still have', trails_left, 'unsuccessful guess(es) before you\n'
              'LOSE the game!')

    print()
    print()


def Report_current_status(current_status, letter, position):
    print('Here is what you currently know about the secret word:')

    if len(position) != 0:
        for i in range(len(position)):
            current_status[position[i]] = letter

    for k in range(len(current_status)):
        print(current_status[k], end = '')
    print()
    print()

    return current_status


def Play_again():
    answer = str(input('Play another game? (y/n) \n'
                       '     '))
    print()
    print()
    print()

    if answer == 'y':
        main()

    print('Thanks for playing Hangman!')


def Play_the_game(secret_word, N):
    current_status = []
    for _ in range(len(secret_word)):
        current_status = current_status + ['-']

    letter = None
    position = []
    input_letters = []
    unfilled_space = len(secret_word)

    while True:
        current_status = Report_current_status(current_status, letter, position)

        letter = Get_an_effective_guess(input_letters)

        input_letters = input_letters + [letter]

        [answer, position] = Check_the_letter(secret_word, letter)

        trails_left = N - len(input_letters)
        Report_each_guess(answer, letter, trails_left)

        unfilled_space = unfilled_space - len(position)
        if unfilled_space == 0:
            print('You win! The secret word was:', secret_word)
            break

        if trails_left == 0:
            print('You lose! The secret word was:', secret_word)
            break

    print()

main()

####### Do NOT attempt this assignment before class! #######

