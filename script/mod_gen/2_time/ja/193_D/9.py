def main():
    K = int(input())
    S = input()
    T = input()
    # 1. 1~9のカードの枚数をカウント
    # 2. 1~9のカードから4枚を選ぶ組み合わせを計算
    # 3. 1. 2. で計算した値を用いて、勝率を計算
    # 4. 3. で計算した勝率を出力
    # 1. 1~9のカードの枚数をカウント
    # 1-1. S, Tの5文字目を除く4文字目を数値に変換
    # 1-2. 1~9のカードの枚数をカウント
    s = [int(i) for i in S[:4]]
    t = [int(i) for i in T[:4]]
    s_count = [s.count(i) for i in range(1, 10)]
    t_count = [t.count(i) for i in range(1, 10)]
    # 2. 1~9のカードから4枚を選ぶ組み合わせを計算
    # 2-1. 1~9のカードの枚数がK枚以下であるかチェック
    # 2-2. 1~9のカードから4枚を選ぶ組み合わせを計算
    s_comb = 1
    t_comb = 1
    for i in range(1, 10):
        if s_count[i-1] + t_count[i-1] < K:
            s_comb *= s_count[i-1] + t_count[i-1] + 1
            t_comb *= s_count[i-1] + t_count[i-1] + 1
        elif s_count[i-1] + t_count[i-1] == K:
            s_comb *= s_count[i-1] + 1
            t_comb *= t_count[i-1] + 1
        else:
            s_comb *= 0
            t_comb *=

if __name__ == '__main__':
    main()