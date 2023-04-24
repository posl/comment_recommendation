Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #print(N, M)
    #print(P)
    #print(Y)

    #県ごとの市の数を求める
    P_count = [0] * N
    for i in range(M):
        P_count[P[i] - 1] += 1
    #print(P_count)

    #県ごとの市の誕生順を求める
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい
    #県ごとの市の誕生順は、県の番号でソートした時の、市の番号の順番に等しい

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #print(P, Y)

    #問題文
    #市 i が 県 P_i に属する市の中で x 番目に誕生した市のとき、市 i の認識番号の上 6 桁は P_i、下 6 桁は x となります。
    #ただし、P_i や x が 6 桁に満たない場合は 6 桁になるまで 0 を左に追加するものとします。

    #県の数
    #N = 2
    #市の数
    #M = 3
    #県
    #P = [1, 2, 1]
    #市が誕生した年
    #Y = [32, 63, 12]

    #県の数
    #N = 2
    #市の数
    #M = 3
    #県
    #P = [2, 2, 2]
    #市が誕生した年
    #Y = [55, 77, 99]

    #県の数
    #N = 3
    #市の数
    #M = 4
    #県
    #P = [1, 1, 2, 3]
    #市が誕生した年
    #Y = [32, 21, 23, 40]

    #県の数
    #N = 3
    #市の数
    #M = 4
    #県
    #P = [2, 2, 2, 1]
    #市が誕生した年
    #Y = [55, 77, 99, 50]

    #県の数
    #N = 3
    #市の数
    #M = 4
    #県
    #P = [3,

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #県ごとに市を分ける
    P_list = [[] for i in range(N+1)]
    for i in range(M):
        P_list[P[i]].append(Y[i])
    #県ごとに市を誕生年の昇順に並べる
    for i in range(1, N+1):
        P_list[i].sort()
    #県ごとに市を誕生年の昇順に並べた結果を使って、市の認識番号を求める
    for i in range(M):
        print('{:06}{:06}'.format(P[i], P_list[P[i]].index(Y[i])+1))

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    # ある県の市の誕生年を格納するリスト
    city = [[] for _ in range(N)]
    for i in range(M):
        city[P[i] - 1].append(Y[i])
    # ある県の市の誕生年のリストを誕生年の昇順にソート
    for i in range(N):
        city[i].sort()
    for i in range(M):
        # 誕生年のリストの何番目にあるかを出力
        print("{:0=6}{:0=6}".format(P[i], city[P[i] - 1].index(Y[i]) + 1))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #print(P)
    #print(Y)
    #県ごとに市を分類
    d = {}
    for i in range(M):
        if P[i] in d:
            d[P[i]].append(Y[i])
        else:
            d[P[i]] = [Y[i]]
    #print(d)
    #市を誕生年順にソート
    for i in range(1, N+1):
        if i in d:
            d[i].sort()
    #print(d)
    #市に認識番号を付与
    for i in range(M):
        print("{:06}{:06}".format(P[i], d[P[i]].index(Y[i])+1))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    Y = [0] * (N + 1)
    for m in range(M):
        P, Y = map(int, input().split())
        Y[P] += 1
        print(str(P).zfill(6) + str(Y[P]).zfill(6))

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for _ in range(M)]

    #県ごとに市をソート
    PY.sort(key=lambda x: x[0])
    #print(PY)

    #市ごとの認識番号を格納するリスト
    ans = [0] * M

    #県ごとに市の番号を振り分ける
    for i in range(M):
        if i == 0:
            #最初の市の場合
            ans[i] = str(PY[i][0]).zfill(6) + str(1).zfill(6)
            #print(ans[i])
        elif PY[i][0] != PY[i - 1][0]:
            #県が変わった場合
            ans[i] = str(PY[i][0]).zfill(6) + str(1).zfill(6)
            #print(ans[i])
        else:
            #県が変わらない場合
            ans[i] = str(PY[i][0]).zfill(6) + str(int(ans[i - 1][6:]) + 1).zfill(6)
            #print(ans[i])

    #出力
    for i in range(M):
        print(ans[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    #入力を受け取る
    input_list = []
    for i in range(M):
        P, Y = map(int, input().split())
        input_list.append([P, Y, i])
    #入力を県ごとに分ける
    input_list.sort(key=lambda x: x[0])
    input_list2 = []
    temp = [input_list[0]]
    for i in range(1, M):
        if input_list[i][0] != input_list[i-1][0]:
            input_list2.append(temp)
            temp = [input_list[i]]
        else:
            temp.append(input_list[i])
    input_list2.append(temp)
    #県ごとに誕生年でソート
    for i in range(len(input_list2)):
        input_list2[i].sort(key=lambda x: x[1])
    #誕生順に番号を振る
    ans = [0]*M
    for i in range(len(input_list2)):
        for j in range(len(input_list2[i])):
            ans[input_list2[i][j][2]] = str(input_list2[i][j][0]).zfill(6) + str(j+1).zfill(6)
    #出力
    for i in range(M):
        print(ans[i])

main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #市の誕生年のリスト
    Y = []
    #県の市の数のリスト
    P = [0] * N
    for _ in range(M):
        p, y = map(int, input().split())
        Y.append([p, y])
        P[p - 1] += 1
    #県の市の数の累積和リスト
    P = [0] + list(accumulate(P))
    #市の認識番号のリスト
    ans = []
    for p, y in Y:
        ans.append(str(p).zfill(6) + str(P[p - 1]).zfill(6))
        P[p - 1] += 1
    for a in ans:
        print(a)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #県ごとの市の数を格納するリスト
    #県番号は1から始まるので、県の数+1の長さのリストを用意する
    #県番号はインデックスとして利用するので、インデックスが0の要素は0としておく
    city_count = [0] * (N+1)
    #市の認識番号を格納するリスト
    #市番号は1から始まるので、市の数+1の長さのリストを用意する
    #市番号はインデックスとして利用するので、インデックスが0の要素は0としておく
    city_id = [0] * (M+1)
    #市の誕生年を格納するリスト
    #市番号は1から始まるので、市の数+1の長さのリストを用意する
    #市番号はインデックスとして利用するので、インデックスが0の要素は0としておく
    city_birth = [0] * (M+1)
    #市の県番号を格納するリスト
    #市番号は1から始まるので、市の数+1の長さのリストを用意する
    #市番号はインデックスとして利用するので、インデックスが0の要素は0としておく
    city_prefecture = [0] * (M+1)

    #市の誕生年と県番号を入力する
    for i in range(1, M+1):
        city_prefecture[i], city_birth[i] = map(int, input().split())

    #市の誕生年でソートする
    #市の誕生年が同じ場合は、市の番号でソートする
    #市の誕生年と市の番号は、市の番号が1
