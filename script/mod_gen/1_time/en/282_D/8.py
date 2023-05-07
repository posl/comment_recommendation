def main():
    #input
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    #edge info
    edgeinfo = [[] for _ in range(N+1)]
    for i in range(M):
        edgeinfo[edges[i][0]].append(edges[i][1])
        edgeinfo[edges[i][1]].append(edges[i][0])
    #connected info
    connected = [0 for _ in range(N+1)]
    connect = 1
    for i in range(1, N+1):
        if connected[i] == 0:
            connected[i] = connect
            connect += 1
            stack = [i]
            while stack:
                now = stack.pop()
                for j in edgeinfo[now]:
                    if connected[j] == 0:
                        connected[j] = connected[now]
                        stack.append(j)
    #bipartite info
    bipartite = [0 for _ in range(N+1)]
    bipartite[1] = 1
    stack = [1]
    while stack:
        now = stack.pop()
        for i in edgeinfo[now]:
            if bipartite[i] == 0:
                bipartite[i] = -bipartite[now]
                stack.append(i)
    #output
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if connected[i] != connected[j] and bipartite[i] != bipartite[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()