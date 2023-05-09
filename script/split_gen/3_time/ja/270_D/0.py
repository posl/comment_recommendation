def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i - A[j]] == 0:
                    dp[i] = 1
                    break
    if dp[N] == 0:
        print("Takahashi")
    else:
        print("Aoki")
