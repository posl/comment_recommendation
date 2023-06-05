def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    s = ''.join(s)
    return int(s)

if __name__ == '__main__':
    g1()