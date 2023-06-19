def g1(x):
    l = list(str(x))
    l.sort(reverse=True)
    return int(''.join(l))

if __name__ == '__main__':
    g1()