def main():
    N = int(input())
    A = []
    for i in range(N):
        T, K = map(int, input().split())
        a = list(map(int, input().split()))
        A.append((T, K, a))
    dp = [0] * N
    dp[0] = A[0][0]
    for i in range(1, N):
        dp[i] = dp[i-1] + A[i][0]
        for j in range(A[i][1]):
            dp[i] = min(dp[i], dp[A[i][2][j]-1] + A[i][0])
    print(dp[N-1])
