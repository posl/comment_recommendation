Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    for _ in range(2):
        dp = [[float('inf')] * (W + 1) for _ in range(H + 1)]
        for i in range(H):
            for j in range(W):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + C
                ans = min(ans, dp[i + 1][j + 1] + A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

=======
Suggestion 2

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i:
                    ans = min(ans, A[i][j]+A[i-1][j]+C)
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+C, A[i][j])
                if j:
                    ans = min(ans, A[i][j]+A[i][j-1]+C)
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+C, A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

=======
Suggestion 3

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18]*W for i in range(H)]
        for i in range(H):
            for j in range(W):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                ans = min(ans, dp[i][j] + A[i][j])
        A = A[::-1]
    print(ans)

=======
Suggestion 4

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18

    for _ in range(2):
        dp = [[10**18] * (w+1) for _ in range(h+1)]
        for i in range(h):
            for j in range(w):
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + c
                ans = min(ans, dp[i+1][j+1] + a[i][j])
        a = [a[i][::-1] for i in range(h)]
    print(ans)

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))

    print(min_cost)

=======
Suggestion 6

def solve(h, w, c, a):
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i==i2 and j==j2:
                        continue
                    ans = min(ans, a[i][j]+a[i2][j2]+c*(abs(i-i2)+abs(j-j2)))
    return ans

=======
Suggestion 7

def main():
    # 標準入力の取得
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    # 処理
    min_cost = 10 ** 9 + 1
    for i1 in range(h):
        for j1 in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i1 == i2 and j1 == j2:
                        continue
                    cost = a[i1][j1] + a[i2][j2] + c * (abs(i1-i2) + abs(j1-j2))
                    if cost < min_cost:
                        min_cost = cost

    # 標準出力
    print(min_cost)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = 10**18
    for h in range(H):
        for w in range(W):
            if h + 1 < H:
                min_cost = min(min_cost, A[h][w] + A[h + 1][w] + C)
            if w + 1 < W:
                min_cost = min(min_cost, A[h][w] + A[h][w + 1] + C)
            if h - 1 >= 0:
                min_cost = min(min_cost, A[h][w] + A[h - 1][w] + C)
            if w - 1 >= 0:
                min_cost = min(min_cost, A[h][w] + A[h][w - 1] + C)
    print(min_cost)

=======
Suggestion 9

def main():
    h, w, c = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))

    min_cost = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(min_cost)

=======
Suggestion 10

def main():
    H, W, C = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]

    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                ans = min(ans, dp[i][j] + A[i][j])
        A = A[::-1]
    print(ans)
