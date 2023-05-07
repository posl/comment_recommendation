def solve(n, p):
    ans = 0
    m = p[0]
    for i in range(n):
        if m >= p[i]:
            ans += 1
            m = p[i]
    return ans
