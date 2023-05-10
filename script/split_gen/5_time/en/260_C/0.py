def solve(n, x, y):
    if x > y:
        return 0
    elif x == y:
        return (n - 1) * x
    else:
        return (n - 1) * x + y
