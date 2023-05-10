def solve(a,n):
    if n == 1:
        return 0
    if a == 1:
        return -1
    x = 1
    for i in range(1,100):
        x = x*a
        if x == n:
            return i
        if x > n:
            break
    x = a
    for i in range(1,100):
        x = x*a
        if x == n:
            return i+1
        if x > n:
            break
    return -1
