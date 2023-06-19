def solve():
    N, X, Y = map(int, input().split())
    dist = [0 for _ in range(N)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            if i <= X <= j or i <= Y <= j:
                dist[min(j-i, abs(X-i)+1+abs(Y-j))] += 1
            else:
                dist[j-i] += 1
    for i in range(1, N):
        print(dist[i])
solve()
