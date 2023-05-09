def main():
    N = int(input())
    A = [[0] * (2*N) for _ in range(2*N)]
    for i in range(2*N):
        A[i] = list(map(int, input().split()))
    dp = [[0] * (2**N) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(2**N):
            if i == 0:
                dp[i][j] = 0
            else:
                for k in range(2*N):
                    if j & 2**k == 0:
                        for l in range(k+1, 2*N):
                            if j & 2**l == 0:
                                dp[i][j] = max(dp[i][j], dp[i-1][j + 2**k + 2**l] ^ A[k][l])
    print(dp[N][0])

if __name__ == '__main__':
    main()