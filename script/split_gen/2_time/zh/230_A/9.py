def solve(s, k):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(n - 1):
        if s[i] == 'X' and s[i + 1] == 'X':
            ans -= 1
    for i in range(n):
        if s[i] == '.':
            if i > 0 and s[i - 1] == 'X':
                ans += 1
            if i < n - 1 and s[i + 1] == 'X':
                ans += 1
    ans = min(ans + k * 2, n)
    return ans
