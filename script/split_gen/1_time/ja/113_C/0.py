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
