def main():
    L = int(input())
    dp = [0] * (L + 1)
    dp[0] = 1
    for i in range(L):
        for j in range(11):
            if i + j + 1 <= L:
                dp[i + j + 1] += dp[i]
    print(dp[L])
