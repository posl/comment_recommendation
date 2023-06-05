def min_energy(x, p):
    e = 0
    for i in x:
        e += (i - p) ** 2
    return e
