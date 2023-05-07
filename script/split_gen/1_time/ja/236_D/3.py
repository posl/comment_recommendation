def main():
    N = int(input())
    A = []
    for i in range(2*N):
        A.append(list(map(int, input().split())))
    dp = [[0]*(2**N) for _ in range(2*N)]
    for i in range(2*N):
        for j in range(2*N):
            if i < j:
                dp[i][j] = A[i][j-1-i]
    for i in range(2*N):
        for j in range(2*N):
            if i < j:
                if (i & j) == 0:
                    dp[i][j] += dp[i][j^(i|j)]
    print(max(dp[i][j] for i in range(2*N) for j in range(2*N) if i < j))
