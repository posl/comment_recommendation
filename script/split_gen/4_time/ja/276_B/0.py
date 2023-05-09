def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 都市の隣接リストを作成
    city = [[] for _ in range(N)]
    for i in range(M):
        city[A[i] - 1].append(B[i])
        city[B[i] - 1].append(A[i])
    # 隣接リストを昇順にソート
    for i in range(N):
        city[i].sort()
    # 出力
    for i in range(N):
        print(len(city[i]), end=' ')
        for j in range(len(city[i])):
            print(city[i][j], end=' ')
        print()
