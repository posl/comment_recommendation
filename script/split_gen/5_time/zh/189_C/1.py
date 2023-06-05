def solve(n, a):
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x * (j - i + 1))
    return ans
