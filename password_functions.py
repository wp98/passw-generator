import random
import string
import datetime


def check_previous(prev_list, index):  # checking previous index to get rid of
    # to much same type of characters next to each other
    amount = 0  # amount of adjacent elements
    for i in range(len(prev_list)):
        if prev_list[i] == index:
            amount += 1
            if amount > 2:
                return True
        else:
            amount = 0
    return False


def check_repeated(passw, char): # check if any of characters has repeated
    for i in range(len(passw)):
        if passw[i] == char:
            return True
    return False


def shuffle_password(password):
    passw_list = list(password)
    random.shuffle(passw_list)
    shuffled = ''.join(passw_list)

    return shuffled


def generate_password(passw_length):
    if passw_length < 8:
        print('Password lenght too short!')
        return False
    passw = ''
    previous_type = []  # list of previous type
    char = ''
    characters = [string.ascii_letters, '0123456789', '!@#$%&*(){}[]']
    for i in range(passw_length):
        type = random.randint(0, 2)  # random choosing type of sing
        previous_type.append(type)
        while check_previous(previous_type, type):
            type = random.randint(0, 2)
        index = random.randint(0, len(characters[type]) - 1)
        char = characters[type][index]
        while check_repeated(passw, char):
            index = random.randint(0, len(characters[type]) - 1)
            char = characters[type][index]
        passw += char
    return passw


def store(passw):
    file = open('secret.txt', 'a+')
    file.write(f'{passw} - {datetime.datetime.now()}')
    file.close()