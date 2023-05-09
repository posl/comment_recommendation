def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False]*(N+1)
    for i in range(N+1):
        for a in A:
            if i-a >= 0:
                dp[i] |= not dp[i-a]
            else:
                break
    print("Takahashi" if dp[N] else "Aoki")
