def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    # A[i]の出現回数をカウント
    count = [0 for _ in range(N + 1)]
    for a in A:
        count[a] += 1
    # A[i]が1つだけの場合は0を出力
    for a in A:
        if count[a] == 1:
            print(0)
        else:
            # A[i]が複数ある場合は、N-1個のボールから2つ選ぶ組み合わせからA[i]を除いた組み合わせを引く
            print((N - 1) * (N - 2) // 2 - (count[a] - 1) * (count[a] - 2) // 2)

if __name__ == '__main__':
    main()