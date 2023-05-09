def solve(n):
    ans = 0
    for i in range(1, 19):
        if n < 10**i:
            ans += f(n, i)
            break
        else:
            ans += f(10**i-1, i)
    return ans % 998244353
