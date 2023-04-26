Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    P = np.array(P)
    Y = np.array(Y)
    #県ごとに市の誕生年をソート
    Y_sort = np.argsort(Y[P-1])
    #県ごとに市の誕生年の順位を格納
    Y_rank = np.zeros(M, dtype=np.int64)
    for i in range(N):
        Y_rank[P-1==i] = np.arange(1, np.sum(P-1==i)+1)
    #県と市の順位を合わせて6桁になるように0埋め
    ans = np.char.zfill(np.array(P, dtype=np.str), 6) + np.char.zfill(np.array(Y_rank, dtype=np.str), 6)
    #出力
    for i in ans:
        print(i)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p = np.array(p)
    y = np.array(y)
    # 都道府県ごとに市の誕生年をソート
    p_sorted = np.argsort(p)
    y_sorted = np.argsort(y[p_sorted])
    # 誕生年の順番を都道府県の順番に変換
    y_sorted = p_sorted[y_sorted]
    # 都道府県ごとに市の誕生年の順番を取得
    y_sorted = np.argsort(y_sorted)
    # 認識番号を出力
    for i in range(m):
        print('{:06d}{:06d}'.format(p[i], y_sorted[i] + 1))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    city = [0] * m
    for i in range(m):
        city[i] = [i, p[i], y[i]]
    city.sort(key=lambda x: x[2])
    pre = [0] * (n + 1)
    for i in range(m):
        pre[city[i][1]] += 1
        for j in range(6 - len(str(pre[city[i][1]]))):
            print(0, end='')
        print(pre[city[i][1]], end='')
        for j in range(6 - len(str(city[i][0] + 1))):
            print(0, end='')
        print(city[i][0] + 1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    Y = [0] * M
    P = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())

    # 2次元配列を用意する。県の数だけ行がある。県ごとに市が何個あるかわからないので、列は最大値を入れる。
    arr = [[0] * M for _ in range(N)]

    # 2次元配列に市を入れる。県ごとに市が何個あるかわからないので、市の番号を入れるときに、空いているところに入れる。
    for i in range(M):
        arr[P[i] - 1][i] = Y[i]

    # 2次元配列を県ごとにソートする。
    for i in range(N):
        arr[i].sort()

    # 2次元配列を県ごとに出力する。県ごとに市が何個あるかわからないので、市の番号を出力するときに、空いているところは飛ばす。
    for i in range(M):
        for j in range(N):
            if arr[j][i] == Y[i]:
                print("{:0=6}".format(j + 1) + "{:0=6}".format(i + 1))

=======
Suggestion 5

def main():
    #入力
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #県ごとに市を誕生年順にソート
    P_sort = [[] for i in range(N + 1)]
    for i in range(M):
        P_sort[P[i]].append((i, Y[i]))
    for i in range(1, N + 1):
        P_sort[i] = sorted(P_sort[i], key=lambda x: x[1])
    #出力
    for i in range(1, N + 1):
        for j in range(len(P_sort[i])):
            print("{:06}{:06}".format(i, j + 1))

=======
Suggestion 6

def main():
    #入力
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)

    #市の誕生年順にソート
    index = sorted(range(M), key=lambda x:Y[x])

    #県ごとの誕生市数のカウント
    count = [0] * (N + 1)
    for i in index:
        count[P[i]] += 1

    #県ごとの誕生市数の累積和
    for i in range(1, N + 1):
        count[i] += count[i - 1]

    #市の認識番号の出力
    for i in index:
        print("{0:06}{1:06}".format(P[i], count[P[i]] - count[P[i] - 1]))
        count[P[i]] -= 1

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    P = [0 for i in range(M)]
    Y = [0 for i in range(M)]
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #市の誕生年の昇順にソート
    #ソート前の市の番号を保持
    P_sort = sorted(P)
    Y_sort = sorted(Y)
    P_num = [0 for i in range(M)]
    for i in range(M):
        P_num[i] = P.index(P_sort[i])
    #市の誕生年をソート
    Y_sort = sorted(Y)
    #県の市の数をカウント
    P_count = [0 for i in range(N)]
    for i in range(M):
        P_count[P[i]-1] += 1
    #県の市の数を累積和
    P_count = [0] + P_count
    for i in range(N):
        P_count[i+1] += P_count[i]
    #市の認識番号を出力
    for i in range(M):
        print('{0:06d}'.format(P_sort[i]) + '{0:06d}'.format(P_count[P_sort[i]-1] - P_count[P_sort[i]-2] - (Y_sort.index(Y[P_num[i]]) - P_count[P_sort[i]-1] + M)))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    # 都道府県ごとに誕生年でソート
    city.sort(key=lambda x: x[1])
    # 都道府県ごとの誕生年のリスト
    birth = [[] for _ in range(N + 1)]
    for i in range(M):
        birth[city[i][0]].append(city[i][1])
    # 都道府県ごとに誕生年の順位を求める
    rank = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        birth[i].sort()
        for j in range(len(birth[i])):
            rank[i].append(birth[i].index(city[i - 1][1]) + 1)
    # 認識番号を求める
    for i in range(M):
        print(str(city[i][0]).zfill(6) + str(rank[city[i][0]][i]).zfill(6))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #県ごとに市の数を数える
    pref = [0] * (N+1)
    for i in range(M):
        p, y = map(int, input().split())
        pref[p] += 1
    #県ごとの市の数を累積和にする
    for i in range(1, N+1):
        pref[i] += pref[i-1]
    #市ごとに県と市の番号を出力
    for i in range(M):
        p, y = map(int, input().split())
        print('{:0=6}{:0=6}'.format(p, pref[p-1]+1))
        pref[p-1] -= 1

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #県の市の数を格納するリスト
    city = [0] * N
    #市の認識番号を格納するリスト
    num = [0] * M
    for i in range(M):
        P, Y = map(int, input().split())
        #県の市の数をインクリメント
        city[P - 1] += 1
        #市の認識番号を生成
        num[i] = str(P).zfill(6) + str(city[P - 1]).zfill(6)
    #市の認識番号を出力
    for i in range(M):
        print(num[i])
