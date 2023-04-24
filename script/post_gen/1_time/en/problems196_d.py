Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(H, W, A, B):
    dp = [[[0 for _ in range(2)] for _ in range(W+1)] for _ in range(H+1)]
    dp[0][0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(2):
                if h >= A and w >= B:
                    dp[h][w][k] += dp[h-A][w-B][k]
                if h >= B and w >= A:
                    dp[h][w][k] += dp[h-B][w-A][k]
                if k == 0:
                    dp[h][w][k] += dp[h][w][1]
                dp[h][w+1][k] += dp[h][w][k]
                dp[h+1][w][k] += dp[h][w][k]
    return dp[H][W][0]

H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H * W)):
        cnt = 0
        for j in range(H * W):
            if i >> j & 1:
                cnt += 1
        if cnt != A + B:
            continue
        row = [0] * W
        for j in range(H * W):
            if i >> j & 1:
                row[j % W] += 1
        if max(row) > B:
            continue
        col = [0] * H
        for j in range(H * W):
            if i >> j & 1:
                col[j // W] += 1
        if max(col) > A:
            continue
        ans += 1
    print(ans)

main()

I was able to solve the problem by myself, but I didn't like the code because it was not clear what I was doing.

So I looked at the editorial and found a better solution.

=======
Suggestion 3

def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H * W)):
        cnt = 0
        for j in range(H * W):
            if i >> j & 1:
                cnt += 1
        if cnt == A:
            cnt = 0
            for j in range(H):
                for k in range(W):
                    if i >> (j * W + k) & 1 and i >> (j * W + k + 1) & 1:
                        cnt += 1
            if cnt == B:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve(h, w, a, b):
    if h == 1:
        return 1
    if w == 1:
        return 1
    if a == 0:
        return 1
    if b == 0:
        return 1
    return solve(h - 1, w, a - 1, b) + solve(h, w - 1, a, b - 1)

=======
Suggestion 5

def main():
    h, w, a, b = map(int, input().split())
    print(solve(h, w, a, b))

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(dfs(H, W, A, B))

=======
Suggestion 7

def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) * A * B)

=======
Suggestion 8

def main():
    H, W, A, B = map(int, input().split())

    def f(i, j):
        if j == 0:
            return 1
        elif i == 0:
            return 0
        else:
            return f(i - 1, j) + f(i - 1, j - 1)

    def g(i, j):
        if i == 0:
            return 1
        elif j == 0:
            return 0
        else:
            return g(i - 1, j) + g(i - 1, j - 1)

    ans = 0
    for i in range(H - A):
        ans += f(A, i) * g(B, W - A - i)
    print(ans)

=======
Suggestion 9

def input():
    return sys.stdin.readline()[:-1]

=======
Suggestion 10

def solve(H, W, A, B):
    # DP[i][j][k] := i x j のマス目に、
    # 2 x 1 のマットをk枚使って
    # 1 x 1 のマットを残りで塗りつぶす方法の総数
    DP = [[[0] * (A + 1) for _ in range(W + 1)] for _ in range(H + 1)]
    DP[1][1][0] = 1
    for i in range(H + 1):
        for j in range(W + 1):
            for k in range(A + 1):
                if i > 0 and j > 0:
                    DP[i][j][k] += DP[i - 1][j - 1][k]
                if i > 1 and k > 0:
                    DP[i][j][k] += DP[i - 2][j][k - 1]
                if j > 1 and k > 0:
                    DP[i][j][k] += DP[i][j - 2][k - 1]
    return DP[H][W][A]

H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))
