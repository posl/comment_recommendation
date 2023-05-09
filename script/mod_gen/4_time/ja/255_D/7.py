def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    #xの最大値を求める
    x_max = max(x)
    #aの最大値を求める
    a_max = max(a)
    #aの最大値がxの最大値以下になるまで、aの最大値をxの最大値にする
    while a_max > x_max:
        a_max = a_max // 2
    #aの最大値がxの最大値以下になったら、aの要素を全てxの最大値にする
    for i in range(n):
        if a[i] > x_max:
            a[i] = x_max
    #aの要素を全てxの最大値にした後のaの要素の合計を求める
    a_sum = sum(a)
    #xの要素の合計を求める
    x_sum = sum(x)
    #xの要素の合計がaの要素の合計より大きい場合、xの要素の合計をaの要素の合計にする
    if x_sum > a_sum:
        x_sum = a_sum
    #xの要素の合計がaの要素の合計になるまで、xの要素の合計をaの要素の合計にする
    while x_sum < a_sum:
        x_sum = x_sum + 1
    #xの要素の合計がaの要素の合計になったら、xの要素の合計をxの要素の数で割って、xの要素の平均値を求める
    x_average = x_sum // n
    #xの要素の平均値を出力する
    print(x_average)

if __name__ == '__main__':
    main()