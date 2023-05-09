def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    #友達関係
    rel = [[0] * N for i in range(N)]
    for i in range(M):
        rel[A[i] - 1][B[i] - 1] = 1
        rel[B[i] - 1][A[i] - 1] = 1
    #ブロック関係
    bl = [[0] * N for i in range(N)]
    for i in range(K):
        bl[C[i] - 1][D[i] - 1] = 1
        bl[D[i] - 1][C[i] - 1] = 1
    #友達候補
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if rel[i][j] == 1 and bl[i][j] == 0:
                ans[i] += 1
    for i in range(N):
        ans[i] -= 1
    #友達候補の数
    for i in range(N):
        for j in range(N):
            if rel[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        print(ans[i], end = " ")
    print()

if __name__ == '__main__':
    main()