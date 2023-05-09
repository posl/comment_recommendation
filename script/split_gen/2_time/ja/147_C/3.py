def main():
    N = int(input())
    A = [0]*N
    X = [[] for i in range(N)]
    Y = [[] for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(2**N):
        honest = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j]:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != Y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, honest.count(1))
    print(ans)
