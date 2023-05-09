def g1(x):
    s = str(x)
    return int(''.join(sorted(s, reverse=True)))

if __name__ == '__main__':
    g1()