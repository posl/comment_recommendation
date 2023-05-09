def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x
            Y[i][j] = y
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1:
                        if (i >> (X[j][k] - 1)) & 1 == 0:
                            flag = False
                            break
                    else:
                        if (i >> (X[j][k] - 1)) & 1 == 1:
                            flag = False
                            break
            else:
                for k in range(A[j]):
                    if Y[j][k] == 1:
                        if (i >> (X[j][k] - 1)) & 1 == 1:
                            flag = False
                            break
                    else:
                        if (i >> (X[j][k] - 1)) & 1 == 0:
                            flag = False
                            break
            if flag == False:
                break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
