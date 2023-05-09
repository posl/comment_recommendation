def f(x):
    g1 = sorted([int(i) for i in str(x)],reverse=True)
    g2 = sorted([int(i) for i in str(x)])
    return int("".join([str(i) for i in g1])) - int("".join([str(i) for i in g2]))

if __name__ == '__main__':
    f()