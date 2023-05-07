def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][x - 1] = 1
            Y[i][x - 1] = y
    ans = 0
    for i in range(1 << N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(N):
                    if X[j][k] == 1 and ((i >> k) & 1) != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
