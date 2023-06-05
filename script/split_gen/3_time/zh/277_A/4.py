def solve(n, x, p):
    for i in range(n):
        if p[i] == x:
            return i+1
