"""
Implementation of rock, paper, scissors by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

def play():
    user = input("qual voce escolhe? 'pe' para pedra, 'p' para papel , 't' para tesoura\n")
    computer = random.choice(['pe', 'p', 't'])

    if user == computer:
        return 'It\'s a tie'

    # pe > t, t > p, p > pe
    if is_win(user, computer):
        return 'Voce venceu!'

    return 'Voce perdeu!'

def is_win(player, opponent):
    # return true if player wins
    # pe > t, t > p, p > pe
    if (player == 'pe' and opponent == 't') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'pe'):
        return True

print(play())
