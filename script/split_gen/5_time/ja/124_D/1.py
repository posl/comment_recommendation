def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    # 0の連続数をカウント
    l = 0
    cnt = 0
    zero_cnt = []
    for i in range(N):
        if S[i] == '0':
            l += 1
        else:
            zero_cnt.append(l)
            l = 0
        if i == N-1:
            zero_cnt.append(l)
    #print(zero_cnt)
    # 0の連続数がK回以上ある場合
    if len(zero_cnt) > K:
        # 0の連続数の合計からK回分の0を引く
        zero_cnt_sum = sum(zero_cnt)
        for i in range(K):
            zero_cnt_sum -= zero_cnt[i]
        #print(zero_cnt_sum)
        # 0の連続数の合計からK回分の0を引いた数が答え
        print(zero_cnt_sum)
    # 0の連続数がK回以下の場合
    else:
        # 0の連続数の合計が答え
        print(sum(zero_cnt))
