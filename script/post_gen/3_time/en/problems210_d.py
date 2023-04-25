Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j))
            ans = min(ans, a[i][j] - c * (i + j))
    print(ans)

=======
Suggestion 2

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 3

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    tmp = a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l))
                    ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10 ** 18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 5

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j))
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] - c * (i + j))
    print(ans)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float("inf")

    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))

    print(ans)

=======
Suggestion 7

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = [[float('inf')]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            min_a[i][j] = min(min_a[i-1][j], min_a[i][j-1]) + a[i][j]
    min_b = [[float('inf')]*w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            min_b[i][j] = min(min_b[i+1][j], min_b[i][j+1]) + a[i][j]
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            ans = min(ans, min_a[i][j] + min_b[i][j] - a[i][j])
    for i in range(h):
        for j in range(w):
            ans = min(ans, min_a[i][j] + min_b[i][j] - a[i][j] + c)
    print(ans)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = [min(a) for a in A]
    min_cost = [min(min_cost)] * W
    for i in range(H):
        for j in range(W):
            min_cost[j] = min(min_cost[j], A[i][j])
            if A[i][j] + min_cost[j] - C < 0:
                print(A[i][j] + min_cost[j])
                return
    print(min_cost[0] + C)

=======
Suggestion 9

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 1. 1つ目の駅を決める
    # 2. 2つ目の駅を決める
    # 3. 1つ目の駅と2つ目の駅の距離を計算する
    # 4. 1つ目の駅のコストに2つ目の駅のコストと距離を足したものを計算する
    # 5. 1～4の中で最小のものを出力する

    # 1. 1つ目の駅を決める
    # 1つ目の駅のコストの最小値を求める
    # 1つ目の駅のコストの最小値の座標を求める

    min_cost = float('inf')
    min_cost_coordinate = [0, 0]
    for i in range(H):
        for j in range(W):
            if min_cost > A[i][j]:
                min_cost = A[i][j]
                min_cost_coordinate = [i, j]

    # 2. 2つ目の駅を決める
    # 2つ目の駅のコストの最小値を求める
    # 2つ目の駅のコストの最小値の座標を求める

    min_cost_2 = float('inf')
    min_cost_coordinate_2 = [0, 0]
    for i in range(H):
        for j in range(W):
            if min_cost_2 > A[i][j] and min_cost_coordinate != [i, j]:
                min_cost_2 = A[i][j]
                min_cost_coordinate_2 = [i, j]

    # 3. 1つ目の駅と2つ目の駅の距離を計算する
    distance = abs(min_cost_coordinate[0] - min_cost_coordinate_

=======
Suggestion 10

def main():
    H,W,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]

    #マス(1,1)からマス(i,j)までの最小コスト
    min_cost = [[0] * W for _ in range(H)]
    min_cost[0][0] = A[0][0]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                min_cost[i][j] = min(min_cost[i][j-1],A[i][j])
            elif j == 0:
                min_cost[i][j] = min(min_cost[i-1][j],A[i][j])
            else:
                min_cost[i][j] = min(min_cost[i-1][j],min_cost[i][j-1],A[i][j])

    #マス(H,W)からマス(i,j)までの最小コスト
    min_cost2 = [[0] * W for _ in range(H)]
    min_cost2[H-1][W-1] = A[H-1][W-1]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            elif i == H-1:
                min_cost2[i][j] = min(min_cost2[i][j+1],A[i][j])
            elif j == W-1:
                min_cost2[i][j] = min(min_cost2[i+1][j],A[i][j])
            else:
                min_cost2[i][j] = min(min_cost2[i+1][j],min_cost2[i][j+1],A[i][j])

    #マス(1,1)からマス(i,j)までの最小コスト + マス(H,W)からマス(i,j)までの最小コスト - A[i][j] + C
    ans = float("inf")
    for i in range(H):
        for j in range(W):
            ans = min(ans,min_cost[i][j] + min_cost2[i][j] - A[i][
