def pay(x, coins):
    if x == 0:
        return True
    if len(coins) == 0:
        return False
    for i in range(coins[0][1]+1):
        if pay(x - coins[0][0] * i, coins[1:]):
            return True
    return False

if __name__ == '__main__':
    pay()