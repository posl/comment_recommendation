def is_connect(a, b):
    if (a == 1 and b == 2) or (b == 1 and a == 2):
        return True
    elif (a == 2 and b == 3) or (b == 2 and a == 3):
        return True
    elif (a == 3 and b == 4) or (b == 3 and a == 4):
        return True
    elif (a == 4 and b == 5) or (b == 4 and a == 5):
        return True
    elif (a == 5 and b == 6) or (b == 5 and a == 6):
        return True
    elif (a == 6 and b == 7) or (b == 6 and a == 7):
        return True
    elif (a == 7 and b == 8) or (b == 7 and a == 8):
        return True
    elif (a == 8 and b == 9) or (b == 8 and a == 9):
        return True
    elif (a == 9 and b == 10) or (b == 9 and a == 10):
        return True
    elif (a == 10 and b == 11) or (b == 10 and a == 11):
        return True
    elif (a == 11 and b == 12) or (b == 11 and a == 12):
        return True
    elif (a == 12 and b == 13) or (b == 12 and a == 13):
        return True
    elif (a == 13 and b == 14) or (b == 13 and a == 14):
        return True
    elif (a == 14 and b == 15) or (b == 14 and a == 15):
        return True
    else:
        return False
a, b = map(int, input().split())

if __name__ == '__main__':
    is_connect()