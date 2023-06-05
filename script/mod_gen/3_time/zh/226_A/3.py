def round(x):
    if 0 <= x and x < 100:
        if x < 10:
            return 0
        elif x < 100:
            return 1
        else:
            return 2
    else:
        return -1

if __name__ == '__main__':
    round()