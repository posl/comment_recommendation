def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 2つの数の和の偶奇は、2つの数の偶奇に依存する
    # 2つの数の偶奇が同じなら、その和は偶数
    # 2つの数の偶奇が異なれば、その和は奇数
    # なので、偶数を作るには、
    # 2つの数の偶奇が異なる組み合わせを探せば良い
    # 2つの数の偶奇が異なる組み合わせの中で最大のものを探せば良い
    # ということは、
    # 偶数の数と奇数の数を数えれば良い
    # 偶数の数が1つ以上あれば、偶数の数の中の最大値を出力すれば良い
    # 偶数の数がなければ、-1を出力すれば良い
    even_count = 0
    odd_count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > 0:
        print(max(a))
    else:
        print(-1)

if __name__ == '__main__':
    main()