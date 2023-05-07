def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの最大値を求める
    max_A = max(A)
    # Aの最大値の約数を求める
    # 約数を格納するリスト
    divisors = []
    # 約数の数を格納するリスト
    num_divisors = []
    # 約数の数の合計を格納するリスト
    sum_divisors = []
    # 1からmax_Aまでの数について
    for i in range(1, max_A + 1):
        # 約数を格納するリスト
        divisors.append([])
        # 約数の数を格納するリスト
        num_divisors.append(0)
        # 約数の数の合計を格納するリスト
        sum_divisors.append(0)
        # 1からiまでの数について
        for j in range(1, i + 1):
            # iをjで割り切れるなら
            if i % j == 0:
                # 約数を格納するリストにjを追加
                divisors[i].append(j)
                # 約数の数を格納するリストに1を追加
                num_divisors[i] += 1
    # 約数の数の合計を格納するリストを求める
    for i in range(1, max_A + 1):
        # 1からiまでの数について
        for j in range(1, i + 1):
            # 約数の数の合計を格納するリストにiの約数の数を追加
            sum_divisors[i] += num_divisors[j]
    # 約数の数の合計を格納するリストを求める
    for i in range(1, max_A + 1):
        # 1からiま

if __name__ == '__main__':
    main()