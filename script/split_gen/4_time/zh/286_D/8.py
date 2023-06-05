def check_coins(coins, money):
    if money == 0:
        return True
    if money < 0:
        return False
    if len(coins) == 0:
        return False
    #print(coins, money)
    return check_coins(coins[1:], money) or check_coins(coins[1:], money - coins[0])
