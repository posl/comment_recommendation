def main():
    # N = 3
    # A = [1,1,1]
    # x = [[2],[1],[2]]
    # y = [[1],[1],[0]]
    N = int(input())
    A = []
    x = []
    y = []
    for i in range(N):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    # print(N, A, x, y)
    ans = 0
    for i in range(2**N):
        honest = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[x[j][k]-1] != y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, sum(honest))
    print(ans)

if __name__ == '__main__':
    main()