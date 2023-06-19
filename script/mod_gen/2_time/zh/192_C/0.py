def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

if __name__ == '__main__':
    g1()