def process():
    N, M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    if N >= M:
        return 0
    dist = []
    for i in range(M-1):
        dist.append(X[i+1]-X[i])
    dist.sort(reverse=True)
    return sum(dist[N-1:])
print(process())
