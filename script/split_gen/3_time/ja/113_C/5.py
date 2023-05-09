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
