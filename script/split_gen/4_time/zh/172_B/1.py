def solve(s,t):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1
    return ans
