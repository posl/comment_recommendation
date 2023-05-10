def check(s):
    if s.find("AGC") != -1:
        return False
    if s.find("GAC") != -1:
        return False
    if s.find("ACG") != -1:
        return False
    if s.find("AGAC") != -1:
        return False
    if s.find("AGGC") != -1:
        return False
    if s.find("AGTC") != -1:
        return False
    if s.find("ATGC") != -1:
        return False
    return True
MOD = 10**9+7
N = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
dp[0][3][3][3] = 1
for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0:
                    continue
                for m in range(4):
                    if check(chr(ord("A")+j)+chr(ord("A")+k)+chr(ord("A")+l)+chr(ord("A")+m)):
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[N][j][k][l]
            ans %= MOD
print(ans)

if __name__ == '__main__':
    check()