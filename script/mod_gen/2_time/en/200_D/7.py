def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    MOD = 200
    dp = [[None] * MOD for _ in range(N + 1)]
    dp[0][0] = []
    for i in range(N):
        for j in range(MOD):
            if dp[i][j] is None:
                continue
            dp[i + 1][j] = dp[i][j]
            dp[i + 1][(j + A[i]) % MOD] = dp[i][j] + [i]
    for i in range(MOD):
        if dp[N][i] is None:
            continue
        if len(dp[N][i]) > 1:
            print("Yes")
            print(len(dp[N][i]))
            print(*[a + 1 for a in dp[N][i]])
            print(len(dp[N][i]) - 1)
            print(*[a + 1 for a in dp[N][i][1:]])
            return
    print("No")

if __name__ == '__main__':
    main()