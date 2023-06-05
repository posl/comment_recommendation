def battle(a, b, c, d):
    while True:
        if c <= 0:
            return True
        elif a <= 0:
            return False
        c -= b
        a -= d
