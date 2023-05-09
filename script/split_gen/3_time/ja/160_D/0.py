def main():
    N, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    for k in range(1, N):
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if len(G[i]) == k and len(G[j]) == k:
                    count += 1
        print(count)
