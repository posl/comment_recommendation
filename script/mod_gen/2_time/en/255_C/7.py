def solve(x, a, d, n):
    if a <= x <= a + d * (n - 1):
        return 0
    if x < a:
        return (a - x) // d + 1
    return (x - a) // d + 1

if __name__ == '__main__':
    solve()