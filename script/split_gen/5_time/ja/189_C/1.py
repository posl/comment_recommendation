def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))
    return ans
