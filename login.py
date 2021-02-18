"""
Beginner Python Project using input, print, and conditionals by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

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