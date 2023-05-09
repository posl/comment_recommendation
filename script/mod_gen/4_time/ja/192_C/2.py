def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = int(''.join(x))
    return x

if __name__ == '__main__':
    g1()