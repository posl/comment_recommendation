def problems100_b(d, n):
    if d == 0:
        return n if n != 100 else 101
    elif d == 1:
        return n * 100 if n != 100 else 10100
    elif d == 2:
        return n * 10000 if n != 100 else 1010000

if __name__ == '__main__':
    problems100_b()