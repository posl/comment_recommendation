def solve(n, a):
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    for i in b:
        if b[i] % 2 == 1:
            return i
