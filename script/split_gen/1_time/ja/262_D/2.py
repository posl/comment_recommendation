def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += (A[i-1]*pow(2, N-i, MOD))%MOD
        ans %= MOD
    print(ans)
