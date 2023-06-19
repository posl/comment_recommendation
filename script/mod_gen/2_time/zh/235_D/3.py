def solve(a, n):
    if a == 1:
        return 1
    if a == n:
        return 2
    if a > n:
        return -1
    ans = 1
    x = 1
    while x < n:
        x *= a
        ans += 1
    if x == n:
        return ans
    else:
        return -1

if __name__ == '__main__':
    solve()