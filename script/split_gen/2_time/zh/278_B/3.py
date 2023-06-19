def isConfusingTime(h, m):
    h1 = int(h / 10)
    h2 = h % 10
    m1 = int(m / 10)
    m2 = m % 10
    if (h1 == 0 and m1 == 0):
        if (h2 == 0 and m2 == 0):
            return False
        else:
            return True
    elif (h1 == 1 and m1 == 1):
        if (h2 == 1 and m2 == 1):
            return False
        else:
            return True
    elif (h1 == 2 and m1 == 5):
        if (h2 == 2 and m2 == 5):
            return False
        else:
            return True
    elif (h1 == 8 and m1 == 8):
        if (h2 == 8 and m2 == 8):
            return False
        else:
            return True
    elif (h1 == 9 and m1 == 6):
        if (h2 == 9 and m2 == 6):
            return False
        else:
            return True
    elif (h1 == 6 and m1 == 9):
        if (h2 == 6 and m2 == 9):
            return False
        else:
            return True
    else:
        return False
