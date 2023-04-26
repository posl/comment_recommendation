Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0

    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if (k - i) ** 2 + (l - j) ** 2 == M:
                        if ans[k][l] == -1:
                            ans[k][l] = ans[i][j] + 1
                        else:
                            ans[k][l] = min(ans[k][l], ans[i][j] + 1)

    for i in range(N):
        print(" ".join(map(str, ans[i])))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i - j) % 2 == 0:
                ans[i][j] = (i + j) // 2
            else:
                ans[i][j] = (i + j) // 2 + 1
    for i in range(N):
        print(*ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(abs(i - j), end=" ")
            print()
    elif M == 2:
        for i in range(N):
            for j in range(N):
                print(min(i + j, 2 * N - i - j - 2), end=" ")
            print()
    elif M == 3:
        for i in range(N):
            for j in range(N):
                print(min(i + j, 2 * N - i - j - 2, i + N - j - 1, j + N - i - 1), end=" ")
            print()
    else:
        print(-1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    INF = 10**18
    ans = [[INF]*N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i-k)**2+(j-l)**2 == M:
                        ans[i][j] = min(ans[i][j], ans[k][l]+1)
    for i in range(N):
        print(*ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())

    # 答えを格納する配列
    ans = [[-1] * N for _ in range(N)]

    # 駒を置くマスをキューに入れる
    que = [(0, 0)]

    # キューが空になるまで繰り返す
    while len(que) > 0:
        # キューの先頭を取り出す
        i, j = que.pop(0)

        # すでに答えが出ているマスはスキップ
        if ans[i][j] >= 0:
            continue

        # 答えを出す
        ans[i][j] = int((i**2 + j**2)**0.5)

        # 4 方向のマスに駒を移動させる
        for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            ni = i + di
            nj = j + dj

            # マスが範囲外ならスキップ
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue

            # 答えが出ていないマスをキューに入れる
            if ans[ni][nj] < 0:
                que.append((ni, nj))

    # 答えを出力する
    for i in range(N):
        print(*ans[i])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    INF = 10**9
    # dp[i][j] := (1,1)から(i,j)までの最小操作回数
    dp = [[INF]*N for _ in range(N)]
    dp[0][0] = 0
    # (i,j)に移動できるマスの候補
    for i in range(N):
        for j in range(N):
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di*dj!=0:
                        continue
                    if i+di<0 or j+dj<0 or i+di>=N or j+dj>=N:
                        continue
                    dp[i+di][j+dj] = min(dp[i+di][j+dj], dp[i][j]+1)
    # (i,j)から(i,j)に移動できるマスの候補
    for i in range(N):
        for j in range(N):
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di*dj!=0:
                        continue
                    if i+di<0 or j+dj<0 or i+di>=N or j+dj>=N:
                        continue
                    dp[i+di][j+dj] = min(dp[i+di][j+dj], dp[i][j])

    for i in range(N):
        for j in range(N):
            if dp[i][j] > M:
                dp[i][j] = -1
            else:
                dp[i][j] = M - dp[i][j]
    for i in range(N):
        print(*dp[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # 駒が置かれているマス
    x = 0
    y = 0
    # 駒が置かれているマスからの距離
    distance = [[0]*N for _ in range(N)]
    # 駒が置かれているマスからの距離がMの倍数かどうか
    is_m = [[False]*N for _ in range(N)]
    # 駒が置かれているマスからの距離がMの倍数のマスの数
    count = 0
    # 駒が置かれているマスからの距離がMの倍数のマスの数がN*Nになるまで繰り返す
    while count < N*N:
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新
        else:
            distance[y][x] += 1
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新
        else:
            distance[y][x] += 1
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新

=======
Suggestion 8

def main():
    N, M = map(int, input().split())

    # (i, j) に移動するために必要な操作回数を dp[i][j] に格納
    dp = [[-1] * N for _ in range(N)]

    # (1, 1) に駒があるので、dp[0][0] = 0
    dp[0][0] = 0

    # (1, 1) から (i, j) に移動するには、
    # (1, 1) から (x, y) に移動する必要がある
    # (x, y) から (i, j) に移動する必要がある
    # ということになる
    # このとき、(i, j) と (x, y) の距離は
    # ((i - x) ** 2 + (j - y) ** 2) ** 0.5
    # となる
    # この値を M で割った余りが 0 になるような (x, y) を全て探す
    # このとき、(x, y) から (i, j) に移動するために必要な操作回数は
    # dp[x][y] + 1
    # となる
    for i in range(N):
        for j in range(N):
            for x in range(N):
                for y in range(N):
                    if ((i - x) ** 2 + (j - y) ** 2) % M == 0:
                        if dp[x][y] != -1:
                            if dp[i][j] == -1:
                                dp[i][j] = dp[x][y] + 1
                            else:
                                dp[i][j] = min(dp[i][j], dp[x][y] + 1)

    for i in range(N):
        print(*dp[i])

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    #Mの平方根を求める
    sqrtM = int(M**0.5)
    #マス目の距離を求める
    #マス目の距離は、マス目の座標の差の絶対値を足したもの
    #マス目の座標の差の絶対値は、マス目の座標の差の2乗の平方根に等しい
    #マス目の座標の差の2乗は、マス目の座標の2乗の和からマス目の座標の2乗の差を引いたもの
    #マス目の座標の2乗の和は、マス目の座標の2乗の和は、(マス目の座標の和の2乗)/2
    #マス目の座標の2乗の差は、マス目の座標の2乗の差は、(マス目の座標の差の2乗)/2
    #マス目の座標の2乗の和からマス目の座標の2乗の差を引くと、マス目の座標の差の2乗の平方根が求まる
    #マス目の座標の差の2乗の平方根は、マス目の座標の差の2乗の平方根は、Mの平方根
    #マス目の座標の差の絶対値は、マス目の座標の差の2乗の平方根に等しい
    #マス目の座標の差の絶対値

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 初期化
    # dp[i][j]はマス(i,j)に移動するのに必要な最小操作回数
    # 初期値は-1
    dp = [[-1] * N for i in range(N)]
    # (1,1)に駒があるので初期値は0
    dp[0][0] = 0
    # マス(i,j)に駒を移動させることができるマスを全探索
    for i in range(N):
        for j in range(N):
            # 駒が移動できるマスが存在する場合
            if dp[i][j] != -1:
                # 駒が移動できるマスを全探索
                for k in range(N):
                    for l in range(N):
                        # マス(k,l)がマス(i,j)から距離がMの平方根である場合
                        if (k-i)**2 + (l-j)**2 == M:
                            # マス(k,l)に移動するのに必要な操作回数を計算
                            # マス(i,j)に駒があるのでマス(k,l)に移動するのに必要な操作回数はdp[i][j]+1
                            dp[k][l] = dp[i][j] + 1
    # 出力
    for i in range(N):
        for j in range(N):
            print(dp[i][j], end=' ')
        print()
