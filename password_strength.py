from getpass import getpass
import re


def get_password_strength(password):
    password_strength = 0
    minimum_char_amount = 6
    optimal_char_amount = 8
    if minimum_char_amount <= len(password) < optimal_char_amount:
        password_strength += 2
    elif len(password) < 6:
        pass
    if len(password) >= optimal_char_amount:
        password_strength += 3
    for pattern in ('[a-z]', '[A-Z]', '[0-9]', '[$#@]'):
        if re.search(pattern, password):
            password_strength += 1

    return password_strength


def load_data():

    with open('passwordlist.txt', 'r') as f:
        common_passwords = f.read()

    return common_passwords


def check_password_blacklist(password, common_passwords):
    in_blacklist = re.findall(common_passwords, password)
    if in_blacklist:
        return 0
    else:
        return 2


if __name__ == '__main__':
    print('Please enter your password: ')
    password = getpass()
    common_passwords = load_data()
    strength = get_password_strength(password)
    blacklist = check_password_blacklist(password, common_passwords)
    password_strength_sum = strength + blacklist
    print('Your password strength score is:', password_strength_sum)
