def buy_cake_donut(n):
    for i in range(0, n, 4):
        if (n - i) % 7 == 0:
            return True
    return False
