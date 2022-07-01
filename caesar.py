"""
File: caesar.py
Name: Antina Yeh
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret = int(input('secret number:'))
    code = input("What's the ciphered string?")
    code = code.upper()
    deciphered_string = decipher(code, secret)
    print('The deciphered string is:' + str(deciphered_string))


def decipher(code, secret):
    """
    :param code: str, ciphered string entered by user
    :param secret: str, number of shifts
    :return: str, returns the deciphered string
    """
    ans = ''
    new_alphabet = ALPHABET[len(ALPHABET)-secret:]
    new_alphabet += ALPHABET[:len(ALPHABET)-secret]
    for i in range(len(code)):
        if code[i] == ' ':
            ans += ' '
        else:
            place = new_alphabet.find(code[i])
            if place == -1:
                ans += code[i]
            else:
                ans += ALPHABET[place]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
