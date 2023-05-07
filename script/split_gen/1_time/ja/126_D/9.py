def main():
    N = int(input())
    edge = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        edge[u].append([v,w])
        edge[v].append([u,w])
    dist = [-1]*(N+1)
    dist[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u,w in edge[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + w
                stack.append(u)
    for i in range(1,N+1):
        print(dist[i]%2)
