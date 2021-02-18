import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'É {guess} muito alto (MA), muito baixo (MB ), ou correto (C)?? ').lower()
        if feedback == 'MA':
            high = guess - 1
        elif feedback == 'MB':
            low = guess + 1

    print(f'OBAA ! O computador escolheu o número , {guess}, correto!')


computer_guess(20)