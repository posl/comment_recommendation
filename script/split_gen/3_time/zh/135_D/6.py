def main():
    S = input()
    n = 13
    dp = [0] * n
    dp[0] = 1
    for i in range(len(S)):
        if S[i] == '?':
            dp2 = [0] * n
            for j in range(10):
                for k in range(n):
                    dp2[(k * 10 + j) % n] += dp[k]
                    dp2[(k * 10 + j) % n] %= 1000000007
            dp = dp2
        else:
            dp2 = [0] * n
            for k in range(n):
                dp2[(k * 10 + int(S[i])) % n] += dp[k]
                dp2[(k * 10 + int(S[i])) % n] %= 1000000007
            dp = dp2
    print(dp[5])
