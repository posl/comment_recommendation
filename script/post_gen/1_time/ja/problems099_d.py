Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # D[i][j]: 色iを色jに変えるコスト
    # c[i][j]: (i,j)が色c[i][j]で塗られている
    # 色iを色jに変えるコストがD[i][j]とする
    # 3色のうちに塗り分ける
    # 3色のうち1色に塗り分けるときのコストをそれぞれa,b,cとする
    # 1色に塗り分けるときのコストはa+b+c
    # 1色に塗り分けるときのコストが最小となるように塗り分ける
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を求める
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を求める
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を求める
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を求める
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を求める
    # 1色に塗り分けるときのコストが最小となるように塗り分けるときの塗り分け方を

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    import itertools
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import shortest_path
    from scipy.sparse.csgraph import minimum_spanning_tree
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse.csgraph import connected_co

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 1,2,3の色をそれぞれ0,1,2としておく
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    # 3種類の色のそれぞれのマスの数を数える
    c0 = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            c0[(i+j)%3][c[i][j]] += 1
    # 各色のコストを求める
    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * c0[i][k]
    # 全探索
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    #print(N, C)
    #print(D)
    #print(c)
    for i in range(C):
        for j in range(C):
            D[i][j] = min(D[i][j], D[i][0] + D[0][j])
    #print(D)
    #print(c)
    a = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            a[(i + j) % 3][c[i][j] - 1] += 1
    #print(a)
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                #print(i, j, k)
                x = 0
                for l in range(C):
                    x += D[l][i] * a[0][l]
                    x += D[l][j] * a[1][l]
                    x += D[l][k] * a[2][l]
                ans = min(ans, x)
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * cost[0][l]
                    tmp += D[l][j] * cost[1][l]
                    tmp += D[l][k] * cost[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 前処理
    # 1. 3 で割った余りごとに色を分ける
    # 2. 各色のマスの個数を数える
    # 3. 各色のマスの個数から、各色のマスに塗り替えるときの違和感を求める
    # 4. 3 つの色の違和感の和が最小になるように塗り替える
    # 5. 1 から 4 までを 3 で割った余りごとに繰り返す
    # 6. 5 つの値の和が答え

    # 1. 3 で割った余りごとに色を分ける
    c1 = [[0] * C for _ in range(3)]
    c2 = [[0] * C for _ in range(3)]
    c3 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                c1[c[i][j] - 1][0] += 1
            elif (i + j) % 3 == 1:
                c2[c[i][j] - 1][1] += 1
            else:
                c3[c[i][j] - 1][2] += 1

    # 2. 各色のマスの個数を数える
    for i in range(C):
        for j in range(3):
            c1[i][j] += c1[i][j - 1]
            c2[i][j] += c2[i][j - 1]
            c3[i][j] += c3[i][j - 1]

    # 3. 各

=======
Suggestion 7

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 各色で塗られたマスの数を数える
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1

    # 3色で塗られたマスの数の総和を最小化する塗り方を求める
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * cnt[0][l]
                    tmp += D[l][j] * cnt[1][l]
                    tmp += D[l][k] * cnt[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 3色ごとにマスの個数を数える
    cnt = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%3][c[i][j]-1] += 1

    # 3色のうち2色を選び、それぞれの色に塗り替えるときの違和感の合計の最小値を求める
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if k == i or k == j:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*cnt[0][l]
                    tmp += D[l][j]*cnt[1][l]
                    tmp += D[l][k]*cnt[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # D[i][j] = iからjに塗り替えるときの違和感
    # c[i][j] = (i,j)の色
    # color[i] = iの色を塗り替えるときの違和感の和

    color = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1

    ans = 10**10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    tmp = 0
                    for l in range(C):
                        tmp += D[l][i]*color[0][l]
                        tmp += D[l][j]*color[1][l]
                        tmp += D[l][k]*color[2][l]
                    ans = min(ans, tmp)

    print(ans)

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 1, 2, 3の色について、それぞれの色が選ばれた時のコストを計算
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1

    # コストが最小になるように色を割り当てる
    ans = 10 ** 18
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                tmp += cost[0][i] * D[i][j]
                tmp += cost[1][j] * D[j][k]
                tmp += cost[2][k] * D[k][i]
                ans = min(ans, tmp)

    print(ans)
