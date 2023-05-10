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

if __name__ == '__main__':
    solve()