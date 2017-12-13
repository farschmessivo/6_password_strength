from getpass import getpass
import re


def get_password_strength(password):
    password_strength = 0
    minimum_char_amount = 6
    optimal_char_amount = 8
    if len(password) >= minimum_char_amount:
        password_strength += 2
    if len(password) >= optimal_char_amount:
        password_strength += 3
    for pattern in ('[a-z]', '[A-Z]', '[0-9]', '[$#@]'):
        if re.search(pattern, password):
            password_strength += 1
    return password_strength


def load_data():
    with open('passwordlist.txt', 'r') as file_handler:
        blacklist = file_handler.read().split()
    return blacklist


def check_password_blacklist(password, blacklist):
    if password not in blacklist:
        return 2


if __name__ == '__main__':
    print('Please enter your password: ')
    password = getpass()
    blacklist = load_data()
    strength = get_password_strength(password)
    in_blacklist = check_password_blacklist(password, blacklist)
    password_strength_sum = strength + in_blacklist
    print('Your password strength score is:', password_strength_sum)
