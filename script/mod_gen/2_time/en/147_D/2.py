def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * pow(2, i, MOD)) % MOD
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()