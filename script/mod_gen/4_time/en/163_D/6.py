def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min_ = i * (i - 1) // 2
        max_ = i * (2 * N - i + 1) // 2
        ans += max_ - min_ + 1
        ans %= MOD
    print(ans)
main()
