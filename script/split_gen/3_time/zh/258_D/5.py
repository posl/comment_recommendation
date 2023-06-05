def solve(n,x,ab):
    a = [0] * (n+1)
    b = [0] * (n+1)
    for i in range(n):
        a[i+1] = ab[i][0]
        b[i+1] = ab[i][1]
    ans = 0
    for i in range(1,n+1):
        ans += a[i] + b[i]
    for k in range(1,n+1):
        ans = min(ans, x * a[k] + b[k] * (n - x))
    return ans
