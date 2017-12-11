import sys
import re


def get_password_strength(password):
    password_strength = 0
    for r in ('[a-z]', '[A-Z]', '[0-9]', '[$#@]'):
        if re.search(r, password):
            password_strength += 1
    if len(password) >= 8:
        password_strength += 1


    return password_strength


def check_password_commonality(password):
    matchedpass = False

    common_passwords = [ "123456", "123456789", "qwerty", "12345678", "111111", "1234567890", "1234567",
                            "password", "123123", "987654321", "qwertyuiop", "mynoob", "123321", "666666",
                            "atcskd2w", "7777777", "q2w3e4r", "654321", "555555", "rjs1la7qe", "google",
                            "q2w3e4r5t", "123qwe", "zxcvbnm", "q2w3e"]

    for commonPass in common_passwords:
        if commonPass == password:
            matchedpass = True

    if matchedpass == True:
        return 0
    else:
        return 2


def password_strength_sum(password_strength, password_strength2):
    password_strength_sum = password_strength + password_strength2
    return password_strength_sum

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 password_strength.py <password>")
    password = sys.argv[1]
    strength = get_password_strength(password)
    commonality = check_password_commonality(password)
    password_strength_sum = password_strength_sum(strength, commonality)
    print(password_strength_sum)
