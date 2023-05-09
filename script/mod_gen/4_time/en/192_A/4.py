def get_next_prize(coins):
    if coins % 100 == 0:
        return 0
    else:
        return 100 - (coins % 100)

if __name__ == '__main__':
    get_next_prize()