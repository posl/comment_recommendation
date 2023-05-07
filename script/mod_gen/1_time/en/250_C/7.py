def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    # N個の要素を持つリストを作成
    # 例：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = list(range(N))
    # x[i]の値をインデックスとして、a[i]とa[i+1]の値を入れ替える
    # 例：[1, 2, 3, 4, 5, 7, 6, 8, 10, 9]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    # 1からNまでの整数をインデックスとして、a[i]の値を出力
    # 例：1 2 3 4 5 7 6 8 10 9
    for i in range(1, N+1):
        print(a[i-1]+1, end=' ')

if __name__ == '__main__':
    main()