def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)

if __name__ == '__main__':
    g1()