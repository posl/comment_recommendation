def main():
    n = int(input())
    A = []
    x = []
    y = []
    for i in range(n):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** n):
        honest = [False] * n
        for j in range(n):
            if ((i >> j) & 1):
                honest[j] = True
        flag = True
        for j in range(n):
            if honest[j]:
                for k in range(A[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, honest.count(True))
    print(ans)
