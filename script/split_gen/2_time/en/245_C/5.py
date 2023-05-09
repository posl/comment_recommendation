def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + A
    B = [0] + B
    dp = [[0, 0] for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = min(dp[i-1][0] + abs(A[i] - A[i-1]), dp[i-1][1] + abs(A[i] - B[i-1]))
        dp[i][1] = min(dp[i-1][0] + abs(B[i] - A[i-1]), dp[i-1][1] + abs(B[i] - B[i-1]))
        if dp[i][0] > K and dp[i][1] > K:
            print("No")
            return
    print("Yes")
    return
