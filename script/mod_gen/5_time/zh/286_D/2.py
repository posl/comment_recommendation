def calc_num_of_coins(coins, x):
    num_of_coins = 0
    for i in range(len(coins)):
        num_of_coins += coins[i][1]
        if num_of_coins >= x:
            return i + 1
    return len(coins)

if __name__ == '__main__':
    calc_num_of_coins()