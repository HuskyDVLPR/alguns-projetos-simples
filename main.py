import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Escolha um número entre 1 e {x}: '))
        if guess < random_number:
            print('DEsculpe, escolha denovo. Muito baixo.')
        elif guess > random_number:
            print('Desculpe, escolha denovo. Muito alto')

    print(f'OBAAA, parabéns. você escolheu o numero {random_number} correto!!')

guess(10)