def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    # print(N, M)
    # print(X)
    # print(C)
    # print(Y)
    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i >= C[j] - 1:
                ans += Y[j] * (i - C[j] + 2)
    print(ans)
