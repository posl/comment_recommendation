def main():
    N = int(input())
    P = list(map(int, input().split()))
    # d[i] = j となるように、d の作成
    d = [0] * N
    for i in range(N):
        d[P[i]] = i
    # d[i] = j となるように、d の作成
    # d = [0] * N
    # for i in range(N):
    #     d[P[i]] = i
    # d の中で最小の値を見つける
    min_d = min(d)
    # d の中で最小の値を見つける
    # min_d = min(d)
    # d の中で最小の値を 0 にする
    for i in range(N):
        d[i] -= min_d
    # d の中で最小の値を 0 にする
    # for i in range(N):
    #     d[i] -= min_d
    # d を d の最小の値で割る
    for i in range(N):
        d[i] //= min_d
    # d を d の最小の値で割る
    # for i in range(N):
    #     d[i] //= min_d
    # d を d の最小の値で割った結果、最大の値を見つける
    max_d = max(d)
    # d を d の最小の値で割った結果、最大の値を見つける
    # max_d = max(d)
    # d を d の最小の値で割った結果、最大の値を見つけたときの d の中でのインデックスを見つける
    for i in range(N):
        if d[i] == max_d:
            break
    # d を d の最小の値で割った結果、最大の値を見つけたときの d の中でのインデックスを見つける
    # for i in range(N):
    #     if d[i
