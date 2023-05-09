def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    dist = []
    for i in range(N-1):
        dist.append(X[i+1]-X[i])
        dist.append(Y[i+1]-Y[i])
    dist.sort()
    ans = 0
    for i in range(N-1):
        ans += dist[i]*(N-1-i)
    print(ans)
main()
