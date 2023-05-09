def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        dist = [-1] * N
        dist[i] = 0
        q = [i]
        while q:
            v = q.pop()
            for w in tree[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    q.append(w)
        ans[i] = dist[Y]
    
    for i in range(N):
        if i == X:
            continue
        print(i+1, ans[i])
