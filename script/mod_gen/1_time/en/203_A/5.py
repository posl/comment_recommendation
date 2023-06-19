def dice_game():
    a = input()
    b = input()
    c = input()
    if a == b:
        print c
    elif a == c:
        print b
    elif b == c:
        print a
    else:
        print 0
dice_game()
