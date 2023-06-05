def get_next_prize_coin(x):
    return (100 - (x % 100)) % 100
