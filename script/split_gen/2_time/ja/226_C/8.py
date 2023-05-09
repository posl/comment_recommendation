def main():
    N = int(input())
    T = [0] * (N+1)
    K = [0] * (N+1)
    A = [[0] for _ in range(N+1)]
    for i in range(1, N+1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = T[i] + max(dp[j] for j in A[i])
    print(dp[-1])
