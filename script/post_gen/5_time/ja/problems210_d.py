Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = float('inf')
    for h in range(H):
        for w in range(W):
            for hh in range(h, H):
                for ww in range(w, W):
                    if h == hh and w == ww:
                        continue
                    ans = min(ans, A[h][w] + A[hh][ww] + C * (abs(h - hh) + abs(w - ww)))
    print(ans)

=======
Suggestion 2

def get_input_data():
    # H, W, C
    input_line = input().split()
    H = int(input_line[0])
    W = int(input_line[1])
    C = int(input_line[2])
    # A
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    return H, W, C, A

=======
Suggestion 3

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_cost = 10 ** 9 * 10 ** 9
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    if cost < min_cost:
                        min_cost = cost
    print(min_cost)

=======
Suggestion 4

def main():
    # H, W, C = map(int, input().split())
    # A = [list(map(int, input().split())) for _ in range(H)]
    H, W, C = 3, 3, 1000000000
    A = [[1000000, 1000000, 1], [1000000, 1000000, 1000000], [1, 1000000, 1000000]]
    print(H, W, C)
    print(A)
    # 1行目、1列目、2列目の最小値を求める
    min_1_1 = min(A[0][0], A[0][1], A[1][0])
    min_1_2 = min(A[0][1], A[0][2], A[1][2])
    min_2_1 = min(A[1][0], A[2][0], A[2][1])
    print(min_1_1, min_1_2, min_2_1)
    min_1 = min(min_1_1, min_1_2)
    min_2 = min(min_1_1, min_2_1)
    min_3 = min(min_1_2, min_2_1)
    print(min_1, min_2, min_3)
    # 1行目、1列目、2列目の最小値を求める
    min_1_1 = min(A[0][0], A[0][1], A[1][0])
    min_1_2 = min(A[0][1], A[0][2], A[1][2])
    min_2_1 = min(A[1][0], A[2][0], A[2][1])
    print(min_1_1, min_1_2, min_2_1)
    min_1 = min(min_1_1, min_1_2)
    min_2 = min(min_1_1, min_2_1)
    min_3 = min(min_1_2, min_2_1)
    print(min_1, min_2, min_3)

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_cost = 10**18
    # 縦横の2パターンでループ
    for i in range(2):
        # 1行ずつ読み込む
        for j in range(H):
            # 1行を読み込んで、配列に格納
            row = A[j]
            # 最小値を取得
            min_row = min(row)
            # 最小値のインデックスを取得
            min_row_idx = row.index(min_row)
            # 最小値のインデックスを削除
            del row[min_row_idx]
            # 次の最小値を取得
            next_min_row = min(row)
            # 最小値を取得
            min_col = min_row
            # 最小値のインデックスを取得
            min_col_idx = min_row_idx
            # 最小値のインデックスを削除
            del row[min_col_idx]
            # 次の最小値を取得
            next_min_col = min(row)
            # 最小値の組み合わせを調べる
            min_cost = min(min_cost, min_row + next_min_row + C, min_col + next_min_col + C)
            # 最小値を元に戻す
            row.insert(min_col_idx, min_col)
            row.insert(min_row_idx, min_row)
        # 縦横を入れ替える
        A = list(map(list, zip(*A)))
    print(min_cost)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                    ans = min(ans, dp[i-1][j] + C + A[i][j] + C*j)
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                    ans = min(ans, dp[i][j-1] + C + A[i][j] + C*i)
                dp[i][j] = min(dp[i][j], A[i][j])
                ans = min(ans, A[i][j] + C*i + C*j)
        A = [a[::-1] for a in A[::-1]]
    print(ans)

=======
Suggestion 7

def solve():
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
    return ans

print(solve())

=======
Suggestion 8

def solve():
    import sys
    input = sys.stdin.readline
    H, W, C = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]

    ans = float('inf')
    for i in range(H):
        for j in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i == i2 and j == j2:
                        continue
                    tmp = A[i][j] + A[i2][j2] + C * (abs(i - i2) + abs(j - j2))
                    ans = min(ans, tmp)

    print(ans)

=======
Suggestion 9

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    min_cost = 10**18
    for _ in range(2):
        dp = [[10**18] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                    min_cost = min(min_cost, dp[i][j] + A[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                    min_cost = min(min_cost, dp[i][j] + A[i][j])
                dp[i][j] = min(dp[i][j], A[i][j])
                min_cost = min(min_cost, dp[i][j] + A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(min_cost)

=======
Suggestion 10

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    # 1回目の駅の選び方
    for i in range(H):
        for j in range(W):
            # 2回目の駅の選び方
            for k in range(i, H):
                for l in range(W):
                    # 同じマスを選んだ場合はスキップ
                    if i == k and j == l:
                        continue
                    # 1回目の駅の建設費用
                    cost1 = A[i][j]
                    # 2回目の駅の建設費用
                    cost2 = A[k][l]
                    # 線路の建設費用
                    cost3 = C * (abs(i - k) + abs(j - l))
                    ans = min(ans, cost1 + cost2 + cost3)
    print(ans)
