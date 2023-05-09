def solve(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    if n == 4:
        return x + y + x * (y - 1)
    if n == 5:
        return x + y + x * (y - 1) + x * (y - 1) * (y - 2)
    if n == 6:
        return x + y + x * (y - 1) + x * (y - 1) * (y - 2) + x * (y - 1) * (y - 2) * (y - 3)
    if n == 7:
        return x + y + x * (y - 1) + x * (y - 1) * (y - 2) + x * (y - 1) * (y - 2) * (y - 3) + x * (y - 1) * (y - 2) * (y - 3) * (y - 4)
    if n == 8:
        return x + y + x * (y - 1) + x * (y - 1) * (y - 2) + x * (y - 1) * (y - 2) * (y - 3) + x * (y - 1) * (y - 2) * (y - 3) * (y - 4) + x * (y - 1) * (y - 2) * (y - 3) * (y - 4) * (y - 5)
    if n == 9:
        return x + y + x * (y - 1) + x * (y - 1) * (y - 2) + x * (y - 1) * (y - 2) * (y - 3) + x * (y - 1) * (y - 2) * (y - 3) * (y - 4) + x * (y - 1) * (y - 2) * (y - 3) * (y - 4) * (
