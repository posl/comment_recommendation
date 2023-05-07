def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 体重でソート
    W, S = zip(*sorted(zip(W, S)))
    # 体重の累積和
    W_sum = [0]
    for i in range(N):
        W_sum.append(W_sum[i] + W[i])
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたもの
    W_sum_max = W_sum[-1]
    W_sum_min = W_sum[0]
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分
    W_sum_half = (W_sum_max - W_sum_min) / 2
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を超える体重の累積和の最小値
    W_sum_half_max = W_sum_min + W_sum_half
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を下回る体重の累積和の最大値
    W_sum_half_min = W_sum_max - W_sum_half
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を超える体重の累積和の最小値を超える体重の累積和の最大値
    W_sum_half_max_max = W_sum_half_max + W_sum_half
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたものの

if __name__ == '__main__':
    main()