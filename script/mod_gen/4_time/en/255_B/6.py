def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    P = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 10**18
    for i in range(N-K+1):
        for j in range(i+K-1, N):
            X = [P[k][0] for k in range(i, j+1)]
            Y = [P[k][1] for k in range(i, j+1)]
            X.sort()
            Y.sort()
            for x in range(i, j-K+2):
                for y in range(x+K-1, j+1):
                    ans = min(ans, (X[y]-X[x])*(Y[y]-Y[x]))
    print(ans**0.5)

if __name__ == '__main__':
    solve()