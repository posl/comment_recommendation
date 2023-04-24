Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].add(v-1)
        G[v-1].add(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if j not in G[i]:
                if i not in G[j]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add(v)
        G[v].add(u)

    ans = 0
    for u in range(N):
        for v in range(u + 1, N):
            if v in G[u]:
                continue
            if len(G[u] & G[v]) == 0:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    g = [[] for i in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    ans = 0
    for i in range(1, N + 1):
        for j in g[i]:
            if j > i:
                flag = True
                for k in g[j]:
                    if k in g[i]:
                        flag = False
                        break
                if flag:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = {i: set() for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j not in graph[i]:
                if len(graph[i] & graph[j]) == 0:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(int(N * (N - 1) / 2))
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[1])
    ans = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if [i, j] not in edges and [j, i] not in edges:
                ans += 1
    print(ans)
main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    E = [set() for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u].add(v)
        E[v].add(u)
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j not in E[i]:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort()
    edges = [(u - 1, v - 1) for u, v in edges]
    
    # 1. count the number of edges from u to v
    # 2. count the number of edges from v to u
    # 3. count the number of edges between u and v
    # 4. count the number of edges from v to u
    # 5. count the number of edges between u and v
    # 6. count the number of edges from u to v
    # 7. count the number of edges from v to u
    # 8. count the number of edges between u and v
    # 9. count the number of edges from v to u
    #10. count the number of edges between u and v
    #11. count the number of edges from u to v
    #12. count the number of edges from v to u
    #13. count the number of edges between u and v
    #14. count the number of edges from v to u
    #15. count the number of edges between u and v
    #16. count the number of edges from u to v
    #17. count the number of edges from v to u
    #18. count the number of edges between u and v
    #19. count the number of edges from v to u
    #20. count the number of edges between u and v
    #21. count the number of edges from u to v
    #22. count the number of edges from v to u
    #23. count the number of edges between u and v
    #24. count the number of edges from v to u
    #25. count the number of edges between u and v
    #26. count the number of edges from u to v
    #27. count the number of edges from v to u
    #28. count the number of edges between u and v
    #29. count the number of edges from v to u
    #30. count the number of edges between u and v
    #31. count the number of edges from u to v

=======
Suggestion 8

def main():
    # Read input
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    # Create adjacency list
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # Create a bipartite graph
    bip = [1] * N
    for i in range(N):
        if bip[i] == 1:
            bip[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if bip[v] == 1:
                        bip[v] = 0 if bip[u] == 1 else 1
                        stack.append(v)
                    elif bip[v] == bip[u]:
                        print(0)
                        return

    # Count the number of pairs of integers (u, v) that satisfy the conditions in the problem statement
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if bip[i] != bip[j] and j not in adj[i]:
                ans += 1
    print(ans)

=======
Suggestion 9

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

=======
Suggestion 10

def read_int():
    return int(input())
