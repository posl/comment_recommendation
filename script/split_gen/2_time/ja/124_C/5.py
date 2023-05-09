def main():
    S = input()
    N = len(S)
    # 0 と 1 の数をそれぞれカウント
    count_0 = S.count('0')
    count_1 = N - count_0
    # 0 と 1 の数が少ない方を選ぶ
    print(min(count_0, count_1))
