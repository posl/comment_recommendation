def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 偶数番目の総和を計算
    even_sum = sum([a[i] for i in range(n) if i % 2 == 0])
    # 偶数番目の総和と奇数番目の総和の差分
    diff = [even_sum - sum(a[1::2])]
    # 差分の絶対値の最大値
    max_abs_diff = diff[0]
    for i in range(n - 1):
        # i 番目の要素を -1 倍する
        diff.append(diff[-1] + 2 * a[i])
        # 差分の絶対値の最大値を更新する
        max_abs_diff = max(max_abs_diff, abs(diff[-1]))
    # 偶数番目の総和と奇数番目の総和の差分に最大値を加算したものが答え
    print(even_sum + max_abs_diff)

if __name__ == '__main__':
    main()