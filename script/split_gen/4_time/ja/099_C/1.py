def main():
    n = int(input())
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        base = 1
        while base <= i:
            dp[i] = min(dp[i],dp[i-base]+1)
            base *= 6
        base = 1
        while base <= i:
            dp[i] = min(dp[i],dp[i-base]+1)
            base *= 9
    print(dp[n])
