def pay(money, coin, num):
    if money == 0:
        return True
    if money < 0:
        return False
    if num <= 0 and money >= 1:
        return False
    return pay(money, coin, num-1) or pay(money-coin[num-1], coin, num)
