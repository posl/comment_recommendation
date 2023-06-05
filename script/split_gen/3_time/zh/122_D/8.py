def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    NG = set(['AGC', 'GAC', 'ACG'])
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(k + ord('A')), chr(l + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(k + ord('A')), chr(m + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(l + ord('A')), chr(m + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(k + ord('A')), chr(l + ord('A')), chr(m + ord('A'))])):
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)
