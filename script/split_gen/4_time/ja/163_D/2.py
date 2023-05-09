def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N - i + 1) * (N + i) // 2 + 1
        ans %= MOD
    print(ans)
