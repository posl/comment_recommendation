def round_up(x, k):
    if k == 0:
        return x
    else:
        a = round_up(x, k - 1)
        b = 10 ** k
        return (a + b - 1) // b * b

if __name__ == '__main__':
    round_up()