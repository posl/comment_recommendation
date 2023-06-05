def pay_coin(coins, money):
    if money == 0:
        return True
    if money < 0 or len(coins) == 0:
        return False
    return pay_coin(coins[1:], money - coins[0]) or pay_coin(coins[1:], money)
