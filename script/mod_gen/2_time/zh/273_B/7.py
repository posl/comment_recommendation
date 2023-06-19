def problem273_b(x, k):
    if k == 0:
        return x
    if x % (10 ** k) == 0:
        return x
    else:
        return x - x % (10 ** k) + 10 ** k

if __name__ == '__main__':
    problem273_b()