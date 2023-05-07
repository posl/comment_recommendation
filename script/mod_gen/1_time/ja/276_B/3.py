def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 都市と道路の関係をリストで作成
    city = [[] for i in range(N)]
    for i in range(M):
        city[A[i] - 1].append(B[i])
        city[B[i] - 1].append(A[i])
    # 都市と道路の関係を出力
    for i in range(N):
        print(len(city[i]), end = ' ')
        for j in range(len(city[i])):
            print(city[i][j], end = ' ')
        print()

if __name__ == '__main__':
    main()