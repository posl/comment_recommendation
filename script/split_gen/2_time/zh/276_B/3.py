def main():
    N = 6
    M = 6
    A = [3, 1, 5, 2, 1, 1]
    B = [6, 3, 6, 5, 2, 6]
    # N, M = map(int, input().split())
    # A = [0] * M
    # B = [0] * M
    # for i in range(M):
    #     A[i], B[i] = map(int, input().split())
    # print(N, M)
    # print(A)
    # print(B)
    # 与城市i直接相连的城市数量
    d = [0] * N
    for i in range(M):
        d[A[i] - 1] += 1
        d[B[i] - 1] += 1
    print(d)
    # 与城市i直接相连的城市
    a = [[] for _ in range(N)]
    for i in range(M):
        a[A[i] - 1].append(B[i])
        a[B[i] - 1].append(A[i])
    print(a)
    for i in range(N):
        print(d[i], end=' ')
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
