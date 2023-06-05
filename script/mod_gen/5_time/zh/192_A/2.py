def get_next_prize_coin(x):
    return (100 - (x % 100)) % 100

if __name__ == '__main__':
    get_next_prize_coin()