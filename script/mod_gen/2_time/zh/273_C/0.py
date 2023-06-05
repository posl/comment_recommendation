def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return x + y - x % y

if __name__ == '__main__':
    round_up()