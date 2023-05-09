def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (N + i + 1) * i // 2 - N * (i - 1)
    print(ans % MOD)
