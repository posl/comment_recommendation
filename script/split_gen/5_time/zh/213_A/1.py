def xor(a,b):
    c = 0
    for i in range(8):
        if (a >> i) & 1 != (b >> i) & 1:
            c += 1 << i
    return c
