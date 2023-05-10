def main():
    K = int(input())
    S = input()
    T = input()
    # 高橋くんの手札
    S = S[:4]
    # 青木くんの手札
    T = T[:4]
    # 1-9の枚数
    S_cnt = [0]*10
    T_cnt = [0]*10
    for i in range(4):
        s = int(S[i])
        t = int(T[i])
        S_cnt[s] += 1
        T_cnt[t] += 1
    # 高橋くんの手札の点数
    S_score = 0
    for i in range(1, 10):
        S_score += i*(10**S_cnt[i])
    # 青木くんの手札の点数
    T_score = 0
    for i in range(1, 10):
        T_score += i*(10**T_cnt[i])
    # 高橋くんの勝つ確率
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            # 高橋くんと青木くんの手札の枚数を増やす
            S_cnt[i] += 1
            T_cnt[j] += 1
            # 高橋くんの点数
            tmp_S_score = S_score + i*(10**S_cnt[i]) - i*(10**(S_cnt[i]-1))
            # 青木くんの点数
            tmp_T_score = T_score + j*(10**T_cnt[j]) - j*(10**(T_cnt[j]-1))
            if tmp_S_score > tmp_T_score:
                # 高橋くんの勝ち
                # 高橋くんの手札の枚数を減らす
                S_cnt[i] -= 1
                # 青木くんの手札の枚数を減らす
                T_cnt[j] -= 1
                # 高橋くんの勝つ確率を増やす
