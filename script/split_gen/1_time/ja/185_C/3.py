def main():
    L = int(input())
    if L == 12:
        print(1)
        return
    elif L == 13:
        print(12)
        return
    dp = [0] * (L + 1)
    dp[12] = 1
    dp[13] = 12
    for i in range(14, L + 1):
        dp[i] = dp[i - 1] + dp[i - 3]
    print(dp[L])
