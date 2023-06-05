def solve(n):
    x = 0
    while (x+1)*(x+2)/2 < n:
        x += 1
    return x+1
