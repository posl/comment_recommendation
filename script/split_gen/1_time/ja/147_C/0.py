def main():
    N = int(input())
    A = [0] * N
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and ((i >> (X[j][k] - 1)) & 1) != 1:
                        flag = False
                    if Y[j][k] == 0 and ((i >> (X[j][k] - 1)) & 1) == 1:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
