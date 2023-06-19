Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h,w,k = map(int,input().split())
    c = []
    for i in range(h):
        c.append(input())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i>>x)&1==0 and (j>>y)&1==0 and c[x][y]=='#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 3

def f(h, w, k):
    if k == 0:
        return 1
    if h == 0 or w == 0:
        return 0
    return f(h - 1, w, k) + f(h, w - 1, k) + f(h - 1, w - 1, k - 1) * (h * w - k)

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
print(f(h, w, k))

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1:
                        continue
                    if (j >> l) & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def dfs(h, w, k, c):
    if h == 0 and w == 0:
        if k == 0:
            return 1
        else:
            return 0
    elif h == 0:
        return dfs(h, w-1, k, c)
    elif w == 0:
        return dfs(h-1, w, k, c)
    elif c[h-1][w-1] == "#":
        return dfs(h-1, w, k, c) + dfs(h, w-1, k, c)
    else:
        return dfs(h-1, w, k, c) + dfs(h, w-1, k, c) + dfs(h-1, w-1, k-1, c)

=======
Suggestion 6

def dfs(h, w, k, c):
    if h == 0 and w == 0:
        return 1 if k == 0 else 0
    if h == 0:
        return dfs(w, 0, k, c)
    if w == 0:
        return dfs(h, 0, k, c)
    if k < 0:
        return 0
    if (h, w, k) in c:
        return c[(h, w, k)]
    res = 0
    for i in range(1 << (h + w)):
        cnt = 0
        for j in range(h):
            if (i >> j) & 1:
                cnt += 1
        for j in range(w):
            if (i >> (j + h)) & 1:
                cnt += 1
        for j in range(h):
            for l in range(w):
                if ((i >> j) & 1) and ((i >> (l + h)) & 1):
                    if c[j][l] == '#':
                        cnt -= 1
        if cnt == k:
            res += 1
    c[(h, w, k)] = res
    return res

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
print(dfs(h, w, k, {}))

=======
Suggestion 7

def solve(H, W, K, c):
    # dp[h][w][k] = (h行w列，剩余k个黑色的方块)的方案数
    dp = [[[0 for k in range(K+1)] for w in range(W+1)] for h in range(H+1)]
    dp[0][0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(K+1):
                # 不选
                dp[h+1][w][k] += dp[h][w][k]
                dp[h][w+1][k] += dp[h][w][k]
                # 选
                if c[h][w] == "#":
                    if k+1 <= K:
                        dp[h+1][w][k+1] += dp[h][w][k]
                        dp[h][w+1][k+1] += dp[h][w][k]
    return dp[H][W][K]

H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
print(solve(H, W, K, c))

=======
Suggestion 8

def solve(h, w, k, c):
    # dp[i][j][k] : i行目まで見たときにj個の行を選択し、k個の黒マスになる場合の数
    dp = [[[0 for _ in range(k+1)] for _ in range(w+1)] for _ in range(h+1)]
    dp[0][0][0] = 1
    for i in range(h):
        for j in range(w):
            for l in range(k+1):
                # 何もしない
                dp[i+1][j][l] += dp[i][j][l]
                # 行を選択
                if c[i][j] == "#":
                    dp[i+1][j][l+1] += dp[i][j][l]
                # 列を選択
                dp[i][j+1][l] += dp[i][j][l]
    return dp[h][w][k]
