def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                continue
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    print(dp[h-1][w-1])
