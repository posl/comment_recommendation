def solve():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    m = min(x, y) - n
    if m < 0:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= (n-i)
        ans %= MOD
    for i in range(n):
        ans *= pow(i+1, MOD-2, MOD)
        ans %= MOD
    for i in range(m):
        ans *= (m-i)
        ans %= MOD
    for i in range(m):
        ans *= pow(i+1, MOD-2, MOD)
        ans %= MOD
    print(ans)
MOD = 10**9+7
solve()
