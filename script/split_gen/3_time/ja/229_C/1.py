def main():
    N, W = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [0]*(W+1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + B[i] <= W:
                dp[j+B[i]] = max(dp[j+B[i]], dp[j] + A[i])
    print(max(dp))
