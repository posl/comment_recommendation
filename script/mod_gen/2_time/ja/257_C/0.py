def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # N = 5
    # S = '10101'
    # W = [60, 45, 30, 40, 80]
    # N = 3
    # S = '000'
    # W = [1, 2, 3]
    # N = 5
    # S = '10101'
    # W = [60, 50, 50, 50, 60]
    # 体重の昇順にソート
    W = sorted(W)
    # print(W)
    # 体重の昇順にソートしたときの、各体重の人数を求める
    # 体重が同じ人がいる場合は、同じ体重の人数を加算する
    num = 1
    w = []
    for i in range(N - 1):
        if W[i] == W[i + 1]:
            num += 1
        else:
            w.append(num)
            num = 1
    w.append(num)
    # print(w)
    # 体重の昇順にソートしたときの、各体重の人数の累積和を求める
    # 体重が同じ人がいる場合は、同じ体重の人数を加算する
    w_sum = [w[0]]
    for i in range(1, len(w)):
        w_sum.append(w_sum[i - 1] + w[i])
    # print(w_sum)
    # 体重の昇順にソートしたときの、各体重の人数の累積和のリストを逆順にする
    w_sum = w_sum[::-1]
    # print(w_sum)
    # 体重の降順にソート
    W = sorted(W, reverse=True)
    # print(W)
    # 判定を正しく行える人数の最大値を求める
    # Sのi文字目が0の場合は、W[i]

if __name__ == '__main__':
    main()