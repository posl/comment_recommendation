def solve(x, y):
    MOD = 10**9 + 7
    if (x + y) % 3 != 0:
        return 0
    n = (x + y) // 3
    x = x - n
    y = y - n
    if x < 0 or y < 0:
        return 0
    return combination(n, x, MOD)

if __name__ == '__main__':
    solve()