def solve(x, y):
    if (x + y) % 3 != 0:
        return 0
    n = (x + y) // 3
    m = x - n
    if m < 0 or n < 0:
        return 0
    if 2 * m < n:
        return 0
    return comb(n, m)

if __name__ == '__main__':
    solve()