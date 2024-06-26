def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (i * (N + 1) - i * (i - 1) // 2) - (i * (i - 1) // 2 - (i - 1) * (i - 2) // 2) + 1
    print(ans % MOD)

if __name__ == '__main__':
    main()