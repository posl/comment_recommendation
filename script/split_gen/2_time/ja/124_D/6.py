def main():
    N, K = map(int, input().split())
    S = input()
    # 連続して逆立ちしている人の数を記録するリスト
    count_list = []
    # 連続して逆立ちしている人の数を記録する変数
    count = 0
    # 連続して直立している人の数を記録する変数
    zero_count = 0
    # 連続して逆立ちしている人の数を記録する
    for i in range(N):
        if S[i] == '1':
            count += 1
        else:
            count_list.append(count)
            count = 0
            zero_count += 1
    count_list.append(count)
    # 連続して直立している人の数がKより多い場合、
    # 連続して逆立ちしている人の数がK+1個以上になる
    if zero_count <= K:
        print(N)
        return
    # 連続して直立している人の数がKより少ない場合、
    # 連続して逆立ちしている人の数がK+1個以下になる
    else:
        # 連続して逆立ちしている人の数がK+1個以上になるようにする
        for i in range(zero_count - K):
            count_list.append(0)
        # 連続して逆立ちしている人の数を合計する
        count_list_sum = [0]
        for i in range(len(count_list)):
            count_list_sum.append(count_list_sum[-1] + count_list[i])
        # 連続して逆立ちしている人の数の最大値を求める
        max_count = 0
        for i in range(len(count_list_sum) - K - 1):
            max_count = max(max_count, count_list_sum[i+K+1] - count_list_sum[i])
        print(max_count)
