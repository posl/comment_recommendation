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

if __name__ == '__main__':
    main()