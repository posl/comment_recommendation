def solve():
    N = int(input())
    A = list(map(int,input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = ans * pow(2,N-1,MOD)
    ans %= MOD
    print(ans)
