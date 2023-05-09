def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    #print(edge)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        v = que.pop(0)
        for to in edge[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                que.append(to)
    #print(dist)
    ans = [0] * N
    for i in range(N):
        if dist[i] != -1:
            ans[dist[i]] += 1
    print(*ans[1:])
