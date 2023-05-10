def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    ans = 0
    for i in range(1, N+1):
        for j in range(M):
            if i >= C[j]:
                ans = max(ans, X[i-1]+Y[j]*(i//C[j]))
    print(ans)
