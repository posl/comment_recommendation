Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[i][j][k][l] == 0:
                        continue
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for n in range(N):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for c4 in range(4):
                        if c2 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c2 == 0 and c3 == 1 and c4 == 2:
                            continue
                        if c2 == 2 and c3 == 0 and c4 == 1:
                            continue
                        if c1 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c1 == 0 and c2 == 2 and c4 == 1:
                            continue
                        dp[n+1][c2][c3][c4] += dp[n][c1][c2][c3]
                        dp[n+1][c2][c3][c4] %= MOD
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[N][c1][c2][c3]
                ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2: continue
                        if k == 1 and l == 0 and m == 2: continue
                        if k == 0 and l == 2 and m == 1: continue
                        if j == 0 and l == 1 and m == 2: continue
                        if j == 0 and k == 1 and m == 2: continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        next = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2: continue
                        if k == 0 and j == 1 and m == 2: continue
                        if l == 0 and j == 1 and m == 2: continue
                        if k == 1 and l == 0 and m == 2: continue
                        if k == 0 and l == 2 and m == 1: continue
                        next[l][m][j] += dp[k][l][m]
                        next[l][m][j] %= mod
        dp = next
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    mod = 10**9+7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        dp2 = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if (k == 1 and l == 2 and m == 3) or (k == 2 and l == 1 and m == 3) or (k == 1 and l == 3 and m == 2) or (j == 1 and l == 2 and m == 3) or (j == 1 and k == 2 and m == 3):
                            continue
                        dp2[k][l][m] += dp[j][k][l]
                        dp2[k][l][m] %= mod
        dp = dp2
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] += dp[i - 1] * 4
        if i >= 2:
            dp[i] += dp[i - 2] * 2
        if i >= 3:
            dp[i] += dp[i - 3] * 3
        if i >= 4:
            dp[i] += dp[i - 4] * 2
        dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 8

def check(s):
    if "AGC" in s:
        return False
    for i in range(len(s)-1):
        if s[i:i+2] == "AGC":
            return False
    return True

=======
Suggestion 9

def main():
    n = int(input())
    mod = 10**9+7
    dp = [0]*64
    for i in range(64):
        dp[i] = [0]*64
    dp[0][0] = 1
    for i in range(n):
        for j in range(64):
            for k in range(4):
                if j>>k&1:
                    continue
                nj = (j|1<<k)<<1&63
                if k == 1 and j>>1&1:
                    continue
                if k == 0 and j>>2&1:
                    continue
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= mod
    ans = 0
    for i in range(64):
        ans += dp[n][i]
        ans %= mod
    print(ans)

=======
Suggestion 10

def check(s):
  if s.count("AGC") >= 1:
    return False
  for i in range(len(s)-1):
    if s[i:i+2] == "AGC":
      return False
    if i+3 < len(s):
      if s[i:i+3] == "AGC":
        return False
  return True
