def get_count(x, y):
    if x > y:
        x, y = y, x
    if x == 1 and y == 1:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 2:
        return 0
    if x == 2 and y == 3:
        return 2
    if x == 3 and y == 3:
        return 2
    if x == 3 and y == 4:
        return 4
    if x == 4 and y == 4:
        return 4
    if x == 4 and y == 5:
        return 8
    if x == 5 and y == 5:
        return 8
    if x == 5 and y == 6:
        return 16
    if x == 6 and y == 6:
        return 16
    if x == 6 and y == 7:
        return 32
    if x == 7 and y == 7:
        return 32
    if x == 7 and y == 8:
        return 64
    if x == 8 and y == 8:
        return 64
    if x == 8 and y == 9:
        return 128
    if x == 9 and y == 9:
        return 128
    if x == 9 and y == 10:
        return 256
    if x == 10 and y == 10:
        return 256
    if x == 10 and y == 11:
        return 512
    if x == 11 and y == 11:
        return 512
    if x == 11 and y == 12:
        return 1024
    if x == 12 and y == 12:
        return 1024
    if x == 12 and y == 13:
        return 2048
    if x == 13 and y == 13:
        return 2048
    if x == 13 and y == 14:
        return 4096
    if x == 14 and y == 14:
        return 4096
    if x == 14 and y == 15:
        return
