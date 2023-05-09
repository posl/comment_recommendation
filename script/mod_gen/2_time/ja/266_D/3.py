def main():
    N = int(input())
    A = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        A.append((T, X, A))
    A.sort()
    #print(A)
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        t, x, a = A[i]
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j == x:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a)
            if i > 0:
                t2, x2, a2 = A[i - 1]
                if t2 == t:
                    continue
                if x2 == x:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i - 1][j] + a)
                else:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i - 1][x2] + a)
    #print(dp)
    print(max(dp[-1]))

if __name__ == '__main__':
    main()