def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        honest = [0] * N
        for j in range(N):
            if i & (1 << j):
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(honest))
    print(ans)

if __name__ == '__main__':
    main()