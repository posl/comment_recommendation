Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    for _ in range(2):
        dp = [[float('inf')] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                dp[i][j] = min(dp[i][j], A[i][j])
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
        ans = min(ans, dp[H-1][W-1])
        A = A[::-1]
    print(ans)

=======
Suggestion 2

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * W for _ in range(H)]
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
Suggestion 3

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = 10**18
    for _ in range(2):
        dp = [[10**18 for _ in range(W)] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                ans = min(ans, A[i][j] + C * (i+j) + dp[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

=======
Suggestion 4

def solve():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + C)
                ans = min(ans, dp[i][j] + A[i][j])
        A = A[::-1]
    print(ans)
solve()

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * (W + 1) for _ in range(H + 1)]
        for i in range(H):
            for j in range(W):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + C
                ans = min(ans, dp[i + 1][j + 1] + A[i][j])
        A.reverse()

    print(ans)

=======
Suggestion 6

def main():
    h,w,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    ans = min(ans,a[i][j]+a[k][l]+c*(abs(i-k)+abs(j-l)))
    print(ans)

=======
Suggestion 7

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    # dp[i][j] := マス(i,j)に駅を建設するときの鉄道建設費用の最小値
    dp = [[float('inf') for _ in range(W)] for _ in range(H)]
    ans = float('inf')

    # dp[i][j]の更新
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            ans = min(ans, A[i][j] + C*(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j], A[i][j] - C*(i+j))

    # dp[i][j]の更新
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            ans = min(ans, A[i][j] + C*(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j], A[i][j] - C*(i+j))

    print(ans)

=======
Suggestion 8

def main():
    # 入力
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    # 答えを格納する変数
    ans = float('inf')

    # 左上から右下への移動
    for i in range(H):
        for j in range(W):
            # 右下のマスから左上のマスへの移動
            for k in range(i, H):
                for l in range(j, W):
                    # 駅を建設するマスが同じマスの場合はスキップ
                    if i == k and j == l:
                        continue
                    # 駅を建設するマスが異なるマスの場合は答えを更新
                    ans = min(ans, A[i][j]+A[k][l]+C*(abs(i-k)+abs(j-l)))

    # 出力
    print(ans)

=======
Suggestion 9

def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_cost = 10**9 + 1
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    cost = a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l))
                    min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 10

def solve():
    # ここに書く
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)
