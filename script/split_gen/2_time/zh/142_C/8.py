def solve(n, a):
    b = [None] * n
    for i in range(n):
        b[a[i]-1] = i+1
    return b
