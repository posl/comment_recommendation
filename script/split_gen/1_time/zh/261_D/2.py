def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C, Y = [], []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    ans = 0
    for i in range(N):
        ans += X[i]
        if i + 1 in C:
            ans += max(Y)
    print(ans)
