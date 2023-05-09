def solve(n, m, a):
    a = [0] + a
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i + 1]
    ans = -10 ** 18
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i] + sum(a[i + 1:i + m + 1]) + m * (m + 1) // 2)
    return ans

if __name__ == '__main__':
    solve()