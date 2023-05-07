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

if __name__ == '__main__':
    main()