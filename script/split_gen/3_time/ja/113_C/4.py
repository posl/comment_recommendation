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
