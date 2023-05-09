def g1(x):
    return int(''.join(sorted(str(x))[::-1]))

if __name__ == '__main__':
    g1()