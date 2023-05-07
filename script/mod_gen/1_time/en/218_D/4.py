def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X = sorted(X)
    Y = sorted(Y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += (X[j]-X[i]) * (Y[j]-Y[i])
    print(ans)

if __name__ == '__main__':
    solve()