def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = [False for i in range(N+1)]
    for i in range(1, N+1):
        for a in A:
            if i-a < 0:
                break
            if dp[i-a] == False:
                dp[i] = True
                break
    if dp[N] == True:
        print("Takahashi")
    else:
        print("Aoki")
