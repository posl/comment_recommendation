def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    # N, K = 200000, 200001
    # MOD = 10**9 + 7
    ans = 0
    for k in range(K, N+2):
        min_sum = k * (k - 1) // 2
        max_sum = (N + N - k + 1) * k // 2
        ans += max_sum - min_sum + 1
        ans %= MOD
    print(ans)
