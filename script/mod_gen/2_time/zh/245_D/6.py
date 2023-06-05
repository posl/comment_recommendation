def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 0: A, 1: B
    dp = [[False for _ in range(2)] for _ in range(N)]
    dp[0][0] = dp[0][1] = True
    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                if abs(A[i] - B[i]) <= K:
                    dp[i][j] = True
                    break
    if dp[N-1][0] or dp[N-1][1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()