def main():
    N = int(input())
    A = [0] * N
    x = [[0] * N for i in range(N)]
    y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** N):
        honest = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, honest.count(1))
    print(ans)
