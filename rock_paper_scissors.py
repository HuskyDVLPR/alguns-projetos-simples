
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
