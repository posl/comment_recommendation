def solve(n, x, v, p):
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            return i + 1
    return -1
