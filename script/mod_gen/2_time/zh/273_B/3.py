def round_up(num, i):
    if num % (10 ** i) == 0:
        return num
    else:
        return num + (10 ** i - num % (10 ** i))

if __name__ == '__main__':
    round_up()