import sys
import re


def get_password_strength(password):
    password_strength = 0
    if 6 <= len(password) < 8:
        password_strength += 2
    elif len(password) < 6:
        password_strength += 0
    if len(password) >= 8:
        password_strength += 3
    for pattern in ('[a-z]', '[A-Z]', '[0-9]', '[$#@]'):
        if re.search(pattern, password):
            password_strength += 1

    return password_strength


def check_password_commonality(password):
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


def password_strength_sum(strength, commonality):
    strength_sum = strength + commonality
    return strength_sum

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 password_strength.py <password>")
    password = sys.argv[1]
    strength = get_password_strength(password)
    commonality = check_password_commonality(password)
    password_strength_sum = password_strength_sum(strength, commonality)
    print('Your password strength score is:', password_strength_sum)
