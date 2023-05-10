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
    if (x - a) % d != 0:
        return -1
    ans = 0
    if d > 0:
        if x < a:
            ans += (a - x) // d
            x += ans * d
        if x > a:
            ans += (x - a) // d
            x -= ans * d
        if x != a:
            return -1
        if ans >= n:
            return -1
        ans += (n - ans) // 2
    else:
        if x > a:
            ans += (x - a) // d
            x += ans * d
        if x < a:
            ans += (a - x) // d
            x -= ans * d
        if x != a:
            return -1
        if ans >= n:
            return -1
        ans += (n - ans) // 2
    return ans
x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

if __name__ == '__main__':
    solve()