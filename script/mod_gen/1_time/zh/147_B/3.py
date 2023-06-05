def solve(s):
    n = len(s)
    ans = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()