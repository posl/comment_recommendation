def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    C = []
    for i in range(M):
        c, y = map(int, input().split())
        Y.append(y)
        C.append(c)
    ans = 0
    for i in range(N):
        ans += X[i]
    for i in range(M):
        tmp = 0
        for j in range(N):
            if C[i] == j + 1:
                tmp += X[j]
        tmp += Y[i]
        if ans < tmp:
            ans = tmp
    print(ans)
