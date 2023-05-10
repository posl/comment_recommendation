def g1(x):
    s = str(x)
    s = ''.join(sorted(s, reverse=True))
    return int(s)

if __name__ == '__main__':
    g1()