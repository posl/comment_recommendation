def main():
    import sys
    input = sys.stdin.readline
    S = input().strip()
    mod = 10 ** 9 + 7
    dp = [0] * 13
    dp[0] = 1
    for i in range(len(S)):
        if S[i] == '?':
            tmp = [0] * 13
            for j in range(10):
                for k in range(13):
                    tmp[(k * 10 + j) % 13] += dp[k]
                    tmp[(k * 10 + j) % 13] %= mod
            dp = tmp
        else:
            tmp = [0] * 13
            for k in range(13):
                tmp[(k * 10 + int(S[i])) % 13] += dp[k]
                tmp[(k * 10 + int(S[i])) % 13] %= mod
            dp = tmp
    print(dp[5])
