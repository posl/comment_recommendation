def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min_sum = (i-1)*i//2
        max_sum = (N + N - i + 1) * i // 2
        ans += max_sum - min_sum + 1
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()