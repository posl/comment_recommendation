Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input_data():
    n,m = map(int,input().split())
    return n,m

=======
Suggestion 2

def main():
    N, M = map(int, input().split())

    #県ごとの市の出現順を記録する配列
    pre = [[] for i in range(N)]

    #市ごとの年を記録する配列
    year = []

    for i in range(M):
        P, Y = map(int, input().split())
        P -= 1
        year.append(Y)
        pre[P].append((Y, i))

    #県ごとの市の出現順を年の昇順にソートする
    for i in range(N):
        pre[i].sort()

    for i in range(M):
        P = year[i]
        #県ごとの市の出現順を年の昇順にソートしたものから市の番号を探す
        idx = pre[P-1].index((year[i], i))
        #市の番号は1から始まるので+1する
        idx += 1
        #市の番号を6桁の文字列に変換する
        idx = str(idx).zfill(6)
        #県の番号を6桁の文字列に変換する
        P = str(P).zfill(6)
        print(P + idx)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    #print(p)
    #print(y)
    d = {}
    for i in range(m):
        if p[i] in d:
            d[p[i]].append(y[i])
        else:
            d[p[i]] = [y[i]]
    #print(d)
    for i in d.keys():
        d[i] = sorted(d[i])
    #print(d)
    for i in range(m):
        print(str(p[i]).zfill(6) + str(d[p[i]].index(y[i]) + 1).zfill(6))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #print(P)
    #print(Y)

    P_Y = [(P[i], Y[i]) for i in range(M)]
    #print(P_Y)

    P_Y.sort()
    #print(P_Y)

    d = {}
    for i in range(M):
        p, y = P_Y[i]
        if p not in d.keys():
            d[p] = 1
        else:
            d[p] += 1
        p_y = str(p).zfill(6) + str(d[p]).zfill(6)
        print(p_y)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(m)]
    py.sort(key=lambda x:x[1])
    
    cnt = [0] * (n + 1)
    for p, y in py:
        cnt[p] += 1
        print('{:06}{:06}'.format(p, cnt[p]))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for i in range(m):
        if p_y[i][0] in p_y_dict:
            p_y_dict[p_y[i][0]] += 1
        else:
            p_y_dict[p_y[i][0]] = 1
    ans = []
    for i in range(m):
        ans.append(str(p_y[i][0]).zfill(6)+str(p_y_dict[p_y[i][0]]).zfill(6))
        p_y_dict[p_y[i][0]] -= 1
    for i in range(m):
        print(ans[i])
main()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]

    p_y.sort(key=lambda x: x[1])

    p_count = [0] * n
    city_id = [0] * m

    for i in range(m):
        p_count[p_y[i][0] - 1] += 1
        city_id[i] = '{:06d}{:06d}'.format(p_y[i][0], p_count[p_y[i][0] - 1])

    for i in range(m):
        print(city_id[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]

    city = [[] for _ in range(N)]
    for i in range(M):
        city[P_Y[i][0] - 1].append([P_Y[i][1], i])

    for i in range(N):
        city[i].sort()

    ans = [0] * M
    for i in range(N):
        for j in range(len(city[i])):
            ans[city[i][j][1]] = str(i + 1).zfill(6) + str(j + 1).zfill(6)

    for i in range(M):
        print(ans[i])

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    PY = [list(map(int,input().split())) for i in range(M)]
    dic = {}
    for i in range(1,N+1):
        dic[i] = []
    for i in range(M):
        dic[PY[i][0]].append(PY[i][1])
    for i in range(1,N+1):
        dic[i].sort()
    for i in range(M):
        print(str(PY[i][0]).zfill(6)+str(dic[PY[i][0]].index(PY[i][1])+1).zfill(6))

=======
Suggestion 10

def solve():
    # 入力
    N, M = map(int, input().split())
    PYs = [list(map(int, input().split())) for _ in range(M)]

    # 各県ごとに市を管理する
    # 順に並べ替える
    # 並べ替えた市に認識番号を割り振る
    # それを順に出力する
    # ただし、市が1つも属さない県がある場合に注意する
    # また、市が1つしか属さない県がある場合も注意する
    # 例えば、市が1つしか属さない県の市の認識番号は 000001000001 となる

    # 各県ごとに市を管理する
    PS = [[] for _ in range(N)]
    for P, Y in PYs:
        PS[P - 1].append(Y)

    # 順に並べ替える
    for P in PS:
        P.sort()

    # 並べ替えた市に認識番号を割り振る
    # それを順に出力する
    for P, Y in PYs:
        P -= 1
        x = PS[P].index(Y) + 1
        print(str(P + 1).zfill(6) + str(x).zfill(6))
