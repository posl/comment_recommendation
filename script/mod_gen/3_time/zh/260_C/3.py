def solve(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    if n == 4:
        return x + 2 * y
    if n == 5:
        return x + 3 * y
    if n == 6:
        return 2 * x + 4 * y
    if n == 7:
        return 2 * x + 5 * y
    if n == 8:
        return 3 * x + 6 * y
    if n == 9:
        return 3 * x + 7 * y
    if n == 10:
        return 4 * x + 8 * y

if __name__ == '__main__':
    solve()