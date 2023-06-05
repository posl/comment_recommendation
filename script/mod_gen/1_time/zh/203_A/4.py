def dice_game(a,b,c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return 0

if __name__ == '__main__':
    dice_game()