def solve():
    N, X, Y = map(int, input().split())
    N -= 1
    X -= 1
    Y -= 1
    def solve_(k):
        d = [0] * N
        for i in range(N):
            for j in range(i+1, N):
                d[min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))] += 1
        return d[k]
    for k in range(1, N):
        print(solve_(k))
