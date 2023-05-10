def main():
    # n: 数列の長さ
    # q: 質問の数
    n, q = map(int, input().split())
    # a: 数列
    a = list(map(int, input().split()))
    # x: 質問の数列
    x = [int(input()) for _ in range(q)]
    # count: 質問の数列の要素ごとの最小操作回数
    count = [0] * q
    # 質問の数列の要素ごとに操作回数を求める
    for i in range(q):
        # 質問の数列の要素
        xi = x[i]
        # 操作回数
        cnt = 0
        # 数列の要素ごとに操作回数を求める
        for j in range(n):
            # 数列の要素
            aj = a[j]
            # 操作回数を求める
            cnt += abs(xi - aj)
        # 質問の数列の要素ごとの最小操作回数を求める
        count[i] = cnt
    # 質問の数列の要素ごとの最小操作回数を出力する
    for i in range(q):
        print(count[i])
