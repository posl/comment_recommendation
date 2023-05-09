def solve():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += len(str(i))
    print(ans%MOD)
