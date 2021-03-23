# To generate password: gen [password length]

import password_functions as pf

password = ''

command = input('[CommandLine]: ')

while command != 'quit':  # Simple text interface
    if 'gen' in command:
        command_s = command.split(' ')  # splited command
        password = pf.generate_password(int(command_s[1]))
        print(f'[PASSWORD]: {password}')
        shuffle_decision = input('You wanna shuffle password? [y/n]')
        while shuffle_decision != 'n':
            password = pf.shuffle_password(password)
            print(f'[SHUFFLED PASSWORD]: {password}')
            shuffle_decision = input('You wanna shuffle password? [y/n]')
        store_decision = input('You wanna save password to text file? [y/n]')
        if store_decision == 'y':
            pf.store(password)
        else:
            print(f'[FINAL PASSOWRD]: {password}')
    command = input('[CommandLine]: ')
