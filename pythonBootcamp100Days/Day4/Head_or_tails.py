import random
heads = 1
tails = 2

heads_or_tails = random.randint(1,2)

if heads_or_tails == heads:
    print(f'Your coin: {heads_or_tails}. Your coin flipped to heads.')
else:
    print(f'Your coin: {heads_or_tails}. Your coin flipped to tails.')