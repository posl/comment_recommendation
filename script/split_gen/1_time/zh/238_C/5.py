def solve(n):
    ans = 0
    m = 1
    while n > 0:
        ans += (n % 10) * m
        m = m * 10 + 1
        n //= 10
    return ans
n = int(input())
ans = 0
m = 1
while n > 0:
    ans += solve(min(n, 10**18)) * m
    m = m * 100 + 11
    n //= 100
print(ans % 998244353)
