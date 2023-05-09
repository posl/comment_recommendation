def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, N-i-1, MOD) * A[i] * pow(N, MOD-2, MOD)
        ans %= MOD
    print(ans)
