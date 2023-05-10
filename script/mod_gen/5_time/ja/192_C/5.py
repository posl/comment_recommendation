def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    return int("".join(s))

if __name__ == '__main__':
    g1()