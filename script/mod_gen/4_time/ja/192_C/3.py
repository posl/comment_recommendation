def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = "".join(x)
    return int(x)

if __name__ == '__main__':
    g1()