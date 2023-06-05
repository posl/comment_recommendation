def solve(n):
    s = 0
    for i in range(1, n+1):
        if s > n:
            return i-1
        s += i
    return -1
