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

if __name__ == '__main__':
    main()