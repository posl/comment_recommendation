def dice_probability(a, b):
    if a <= 0:
        return False
    elif a == 1:
        if b <= 6:
            return True
        else:
            return False
    elif a == 2:
        if b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12:
            return True
        else:
            return False
    elif a == 3:
        if b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18:
            return True
        else:
            return False
    elif a == 4:
        if b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18 or b == 19 or b == 20 or b == 21 or b == 22 or b == 23 or b == 24:
            return True
        else:
            return False
    elif a == 5:
        if b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18 or b == 19 or b == 20 or b == 21 or b == 22 or b == 23 or b == 24 or b == 25 or b == 26 or b == 27 or b == 28 or b == 29 or b == 30 or b == 31 or b == 32 or b == 33 or b == 34
