def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += (i+1) * a[i] - sum(a[:i+1])
        ans += sum(a[i+1:]) - (n-i-1) * a[i]
    return ans
