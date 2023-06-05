def solve(x, y):
    if x >= y:
        return 0
    else:
        return (y - x) // 10 + (1 if (y - x) % 10 > 0 else 0)
