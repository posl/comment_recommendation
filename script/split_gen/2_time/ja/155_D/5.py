def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 負の数を含む場合、正の数に変換する
    A = [a if a >= 0 else -a for a in A]
    # 正の数のみの場合は、ソートしてK番目の値を出力する
    if max(A) == 0:
        A.sort()
        print(A[K - 1])
        return
    # 正の数と負の数を分ける
    positive = []
    negative = []
    for a in A:
        if a > 0:
            positive.append(a)
        else:
            negative.append(a)
    # 正の数と負の数を組み合わせて積を求める
    # 正の数の個数と負の数の個数をカウントする
    positive_count = len(positive)
    negative_count = len(negative)
    # 積を格納するリスト
    product_list = []
    # 正の数と負の数の積を求める
    for p in positive:
        for n in negative:
            product_list.append(p * n)
    # 正の数と正の数の積を求める
    for i in range(positive_count - 1):
        for j in range(i + 1, positive_count):
            product_list.append(positive[i] * positive[j])
    # 負の数と負の数の積を求める
    for i in range(negative_count - 1):
        for j in range(i + 1, negative_count):
            product_list.append(negative[i] * negative[j])
    # 積のリストをソートする
    product_list.sort()
    # K番目の値を出力する
    print(product_list[K - 1])
