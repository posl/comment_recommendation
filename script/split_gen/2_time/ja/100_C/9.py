def main():
    # N:数列の長さ
    N = int(input())
    # a:数列
    a = list(map(int, input().split()))
    # 2で割り切れる回数をカウントする変数
    count = 0
    # 数列の各要素に対して、2で割り切れる回数をカウントする
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)
