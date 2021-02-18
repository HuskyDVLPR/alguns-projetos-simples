

import time

username = 'husky'
password = '123'

username_input = input('Nomde de usuário: ')
password_input = input('Senha: ')

if username_input == username and password_input == password:
    print('Acesso garantido')
    print('Por favor, espere')
    time.sleep(5)
    print('Ok... Carregando...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Muito bem, tem autorização de segurança. Puxar para cima o mainframe secreto.')
elif username_input == username and password_input != password:
    print('Senha incorreta')
elif username_input != username and password_input == password:
    print('Nome de usuário incorreto')
else:
    print('Pode querer verificar os dois campos...')