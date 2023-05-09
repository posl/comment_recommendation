def solve(n, a):
    if 0 in a:
        return 0
    result = 1
    for i in range(n):
        result *= a[i]
        if result > 10**18:
            return -1
    return result
