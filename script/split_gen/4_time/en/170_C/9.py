def solve(x, n, p):
    if n == 0:
        return x
    if x not in p:
        return x
    else:
        for i in range(1, 100):
            if x - i not in p:
                return x - i
            elif x + i not in p:
                return x + i
