def g1(x):
    s = list(str(x))
    s.sort(reverse=True)
    return int("".join(s))

if __name__ == '__main__':
    g1()