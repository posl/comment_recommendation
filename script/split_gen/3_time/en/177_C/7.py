def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    # 累積和
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = (s[i - 1] + A[i - 1]) % MOD
    ans = 0
    for i in range(N):
        ans += A[i] * (s[N] - s[i + 1])
        ans %= MOD
    print(ans)
