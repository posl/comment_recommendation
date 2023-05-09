def check(x, t):
    n = len(x)
    m = len(t)
    for i in range(n-m+1):
        if x[i:i+m] == t:
            return False
    return True
