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


def load_blacklist():
    with open('passwordlist.txt', 'r') as file_handler:
        blacklist = file_handler.read().split()
    return blacklist


def check_if_password_is_not_in_blacklist(password, blacklist):
    not_in_blacklist_points = (password not in blacklist) * 2
    return not_in_blacklist_points


if __name__ == '__main__':
    print('Please enter your password: ')
    password = getpass()
    blacklist = load_blacklist()
    strength = get_password_strength(password)
    not_in_blacklist = check_if_password_is_not_in_blacklist(password,
                                                             blacklist)
    password_strength_sum = strength + not_in_blacklist
    print('Your password strength score is:', password_strength_sum)
