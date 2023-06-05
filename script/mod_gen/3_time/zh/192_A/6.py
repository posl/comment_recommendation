def get_extra_coins(coins):
    if coins % 100 == 0:
        return 100
    else:
        return 100 - (coins % 100)

if __name__ == '__main__':
    get_extra_coins()