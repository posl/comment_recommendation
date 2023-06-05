def xor(a,b):
    c = []
    d = []
    for i in range(8):
        c.append(a%2)
        d.append(b%2)
        a = int(a/2)
        b = int(b/2)
    e = []
    for i in range(8):
        if c[i] == d[i]:
            e.append(0)
        else:
            e.append(1)
    f = 0
    for i in range(8):
        f = f + e[i] * (2**i)
    return f
