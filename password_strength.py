from getpass import getpass
import re


def get_password_strength(password):
    password_strength = 0
    absolute_minimum_char = 6
    optimal_char = 8
    if absolute_minimum_char <= len(password) < optimal_char:
        password_strength += 2
    elif len(password) < 6:
        pass
    if len(password) >= optimal_char:
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
    matched_pass = False

    with open('passwordlist.txt', 'r') as f:
        common_passwords = f.read()

        for common_pass in common_passwords:
            if common_pass == password:
                matched_pass = True

    if matched_pass == True:
        return 0
    else:
        return 2


def password_strength_sum(strength, blacklist):
    strength_sum = strength + blacklist
    return strength_sum

if __name__ == '__main__':
    print('Please enter your password: ')
    password = getpass()
    common_passwords = load_data()
    # if len(sys.argv) == 1:
    #     sys.exit("Usage: python3 password_strength.py <password>")
    # password = sys.argv[1]
    strength = get_password_strength(password)
    blacklist = check_password_blacklist(password, common_passwords)
    password_strength_sum = password_strength_sum(strength, blacklist)
    print('Your password strength score is:', password_strength_sum)
