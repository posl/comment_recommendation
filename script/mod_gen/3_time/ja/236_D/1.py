def main():
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]
    B = []
    for i in range(N):
        for j in range(i+1,N):
            B.append(A[i][j-i-1])
    dp = [0]*(1<<N)
    for i in range(1<<N):
        for j in range(N):
            if not i&(1<<j):
                dp[i|(1<<j)] = max(dp[i|(1<<j)],dp[i]^B[j])
    print(dp[-1])

if __name__ == '__main__':
    main()