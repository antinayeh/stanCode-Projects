"""
File: hangman.py
Name: Antina Yeh
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    hint = ('-'*len(word))
    count = 0
    game(word, hint, count)
    print('The word was:', str(word))


def game(word, hint, count):
    """
    :param word: str, random word generated
    :param hint: str, blank lines to hide the answer
    :param count: int, number of wrong guesses
    """
    while True:
        if count == N_TURNS:
            print('You are completely hung:( \n')
            break
        elif hint == word:
            print('You Win!')
            break
        print('The word looks like: ', str(hint), '\nYou have ' + str(N_TURNS - count) + ' guesses left')
        input_ch = input_check()
        if input_ch in word:
            for i in range(len(word)):
                letter = word[i]
                if input_ch == letter:
                    ans = ''
                    ans += hint[:i]
                    ans += input_ch
                    ans += hint[i+len(input_ch):]
                    hint = ans
            print('You are correct!')
        else:
            count += 1
            print('There is no', str(input_ch), "'s in this word")


def input_check():
    """
    This function will check whether the input is illegal or not
    :return: legal user input
    """
    input_ch = input('Your guess:').upper()
    while True:
        if not input_ch.isalpha() or len(input_ch) > 1:
            print('illegal format')
            input_ch = input('Your guess:').upper()
        else:
            break
    return input_ch


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
