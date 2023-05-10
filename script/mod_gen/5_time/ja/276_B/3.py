def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, A, B)
    # 都市と道路の接続情報を管理する配列
    # 1-indexedで管理するため、N+1個の配列を用意
    # 都市iと道路で直接結ばれている都市はd[i]個ある
    d = [0] * (N+1)
    # 都市iと道路で直接結ばれている都市を昇順に管理する
    a = [[] for _ in range(N+1)]
    #print(d, a)
    # 都市iと道路で直接結ばれている都市を配列に格納
    for i in range(M):
        d[A[i]] += 1
        d[B[i]] += 1
        a[A[i]].append(B[i])
        a[B[i]].append(A[i])
    #print(d, a)
    # 出力
    for i in range(1, N+1):
        print(d[i], end = " ")
        for j in range(d[i]):
            print(a[i][j], end = " ")
        print()

if __name__ == '__main__':
    main()