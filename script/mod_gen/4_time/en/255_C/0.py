def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if n == 1:
        if x == a:
            return 0
        else:
            return -1
    if n == 2:
        if x == a:
            return 0
        elif x == a + d:
            return 1
        else:
            return -1
    if n == 3:
        if x == a:
            return 0
        elif x == a + d:
            return 1
        elif x == a + 2 * d:
            return 2
        else:
            return -1
    if a + 2 * d <= x:
        return (x - a) // d
    if a - d <= x <= a + d:
        return 1
    if x < a - d:
        return (a - d - x) // (2 * d) + 1 + (a - d - x) % (2 * d) // d
    return -1
x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

if __name__ == '__main__':
    solve()