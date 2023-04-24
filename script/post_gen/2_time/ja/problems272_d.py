Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if (i ** 2 + j ** 2) == M:
                ans[i][j] = 1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 1:
                continue
            if ans[i][j] == -1:
                ans[i][j] = 2
            for k in range(N):
                for l in range(N):
                    if ans[k][l] == -1:
                        continue
                    if (i - k) ** 2 + (j - l) ** 2 == M:
                        if ans[i][j] == -1:
                            ans[i][j] = ans[k][l] + 1
                        else:
                            ans[i][j] = min(ans[i][j], ans[k][l] + 1)
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end = " ")
        print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            ans[i][j] = (i + j) * (i + j) + (i - j) * (i - j)
    for i in range(N):
        for j in range(N):
            if ans[i][j] == M:
                ans[i][j] = 1
            elif ans[i][j] < M:
                ans[i][j] = 2
            else:
                ans[i][j] = -1
    for i in range(N):
        print(*ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    ans = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                ans[i][j] = (i + j) // 2
            else:
                ans[i][j] = (i + j) // 2 + 1
    for i in range(N):
        for j in range(N):
            if ans[i][j] > M:
                ans[i][j] = -1
    for i in range(N):
        print(*ans[i])

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            print(*[abs(i-j) for j in range(n)])
    else:
        for i in range(n):
            print(*[min(abs(i-j), abs(i-j-n), abs(i-j+n)) for j in range(n)])

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    D = [[10**9]*N for _ in range(N)]
    D[0][0] = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i-k)**2+(j-l)**2 == M:
                        D[i][j] = min(D[i][j],D[k][l]+1)
    for i in range(N):
        print(*D[i])

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    #マスの距離を求める
    def distance(i,j):
        return ((i-1)**2+(j-1)**2)**(1/2)
    #距離がMの倍数かどうかを判定する
    def judge(i,j):
        if distance(i,j) % M == 0:
            return True
        else:
            return False
    #距離がMの倍数のマスを求める
    def judge_list():
        judge_list = []
        for i in range(1,N+1):
            for j in range(1,N+1):
                if judge(i,j):
                    judge_list.append([i,j])
        return judge_list
    #距離がMの倍数のマスを求める
    judge_list = judge_list()
    #距離がMの倍数のマスからの最短距離を求める
    #距離がMの倍数のマスからの最短距離を求める
    def judge_distance(i,j):
        min_distance = 100000
        for k in range(len(judge_list)):
            if min_distance > abs(i-judge_list[k][0])+abs(j-judge_list[k][1]):
                min_distance = abs(i-judge_list[k][0])+abs(j-judge_list[k][1])
        return min_distance
    #距離がMの倍数のマスからの最短距離を求める
    for i in range(1,N+1):
        for j in range(1,N+1):
            if judge(i,j):
                print(0,end=' ')
            else:
                print(judge_distance(i,j),end=' ')
        print()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    # (1,1)からの距離
    d = [[10**9] * N for _ in range(N)]
    d[0][0] = 0
    # (1,1)からの距離がMの平方根となるマスの座標を求める
    for i in range(N):
        for j in range(N):
            if (i**2+j**2) == M:
                ans[i][j] = 1
                d[i][j] = 1
    # 1マスずつ距離を求める
    for i in range(N):
        for j in range(N):
            if i+1 < N:
                if d[i+1][j] > d[i][j] + 1:
                    d[i+1][j] = d[i][j] + 1
            if j+1 < N:
                if d[i][j+1] > d[i][j] + 1:
                    d[i][j+1] = d[i][j] + 1
            if i-1 >= 0:
                if d[i-1][j] > d[i][j] + 1:
                    d[i-1][j] = d[i][j] + 1
            if j-1 >= 0:
                if d[i][j-1] > d[i][j] + 1:
                    d[i][j-1] = d[i][j] + 1
    for i in range(N):
        for j in range(N):
            if d[i][j] == 10**9:
                d[i][j] = -1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 1:
                ans[i][j] = d[i][j]
    for i in range(N):
        print(*ans[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # N = 400, M = 10**6 なので、Mの平方根の整数部分を求める
    M = int(M**0.5)
    # 2次元配列の初期化
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    # 初期位置の設定
    ans[0][0] = 0
    # 1次元配列の初期化
    que = [[0, 0]]
    # Mの平方根の整数部分を超えるまで、1次元配列の要素を取り出す
    while que:
        # 1次元配列の要素を取り出す
        x, y = que.pop(0)
        # 1次元配列の要素を元に、上下左右にMの平方根の整数部分の距離を移動できるかを確認する
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            # 移動先がマス目の範囲外の場合、処理をスキップする
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 移動先が未訪問の場合、移動先の距離を設定する
            if ans[nx][ny] == -1:
                ans[nx][ny] = ans[x][y] + 1
                # 移動先がMの平方根の整数部分の距離である場合、移動先を1次元配列に追加する
                if ans[nx][ny] == M:
                    que.append([nx, ny])
    # 結果を出力する
    for i in range(N):
        print(*ans[i])
