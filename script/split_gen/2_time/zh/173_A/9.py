def solve(n):
    ans = 0
    for i in range(1, n+1):
        ans += i * f(i)
    return ans
