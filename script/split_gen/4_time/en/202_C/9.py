def solve(n, a, b, c):
    ans = 0
    d = {}
    for i in range(n):
        if c[b[i]-1] in d:
            d[c[b[i]-1]] += 1
        else:
            d[c[b[i]-1]] = 1
    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]
    return ans
