def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for _ in range(2**N)] for _ in range(N+1)]
    for i in range(N):
        for j in range(2**i):
            for k in range(2**(N-i-1)):
                dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j] ^ A[i][j+k])
    print(dp[N][2**N-1])

if __name__ == '__main__':
    main()