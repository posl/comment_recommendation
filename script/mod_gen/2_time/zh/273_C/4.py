def round_up(x, i):
    if x % (10 ** i) >= 5 * 10 ** (i - 1):
        return x - x % (10 ** i) + 10 ** i
    else:
        return x - x % (10 ** i)

if __name__ == '__main__':
    round_up()