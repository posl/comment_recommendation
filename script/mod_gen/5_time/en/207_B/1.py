def solve(a, b, c, d):
    if a <= b * d:
        return -1
    else:
        return (a + b - c - 1) // (b - c)

if __name__ == '__main__':
    solve()