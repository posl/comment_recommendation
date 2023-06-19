def g1(x):
    l = []
    while x > 0:
        l.append(x % 10)
        x //= 10
    l.sort(reverse=True)
    return 0 if l[0] == 0 else int(''.join(str(x) for x in l))
