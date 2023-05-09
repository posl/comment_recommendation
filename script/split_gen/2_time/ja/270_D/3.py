def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] == 0:
                dp[i] = 1
                break
    print("Takahashi" if dp[N] else "Aoki")
