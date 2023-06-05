def check(n):
    x = 0
    for i in range(1, n+1):
        x += i
        if x >= n:
            return i
