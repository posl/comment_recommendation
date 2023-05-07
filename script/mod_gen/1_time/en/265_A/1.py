def solve(x, y, n):
    if n % 3 == 0:
        return n / 3 * y
    elif n % 3 == 1:
        return (n - 1) / 3 * y + x
    else:
        return (n - 2) / 3 * y + 2 * x

if __name__ == '__main__':
    solve()