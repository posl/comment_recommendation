def main():
    K = int(input())
    S = input()
    T = input()
    S = S[:4]
    T = T[:4]
    S = list(map(int, S))
    T = list(map(int, T))
    #カードの枚数をカウント
    S_count = [0] * 10
    T_count = [0] * 10
    for s in S:
        S_count[s] += 1
    for t in T:
        T_count[t] += 1
    #各カードの枚数を計算
    S_num = [K - S_count[i] for i in range(1, 10)]
    T_num = [K - T_count[i] for i in range(1, 10)]
    #勝率を計算
    win = 0
    for s in range(1, 10):
        for t in range(1, 10):
            if s == t:
                if S_count[s] + 2 > K or T_count[t] + 2 > K:
                    continue
                win += (S_num[s] / (K * (K - 1))) * (T_num[t] / (K * (K - 1) - 1))
            else:
                if S_count[s] + 1 > K or T_count[t] + 1 > K:
                    continue
                win += (S_num[s] / (K * (K - 1))) * (T_num[t] / (K * (K - 1)))
    print(win)
