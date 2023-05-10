def dfs(cur, prev1, prev2, prev3):
    if cur == n:
        return 1
    if dp[cur][prev1][prev2][prev3] != 0:
        return dp[cur][prev1][prev2][prev3]
    ret = 0
    for c in range(4):
        if prev1 == 0 and prev2 == 1 and prev3 == 3 and c == 2:
            continue
        elif prev1 == 0 and prev2 == 3 and prev3 == 1 and c == 2:
            continue
        elif prev1 == 1 and prev2 == 0 and prev3 == 3 and c == 2:
            continue
        elif prev1 == 0 and prev2 == 1 and prev3 == 2 and c == 3:
            continue
        elif prev1 == 0 and prev2 == 2 and prev3 == 1 and c == 3:
            continue
        ret += dfs(cur + 1, prev2, prev3, c)
        ret %= MOD
    dp[cur][prev1][prev2][prev3] = ret
    return ret
MOD = 10 ** 9 + 7
n = int(input())
dp = [[[[-1] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    dfs()