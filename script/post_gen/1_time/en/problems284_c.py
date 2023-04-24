Synthesizing 10/10 solutions

=======
Suggestion 1

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    used = [False] * N
    ans = 0
    for i in range(N):
        if used[i]:
            continue
        ans += 1
        q = [i]
        while q:
            v = q.pop()
            used[v] = True
            for nv in G[v]:
                if used[nv]:
                    continue
                q.append(nv)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            queue = [i]
            while queue:
                now = queue.pop()
                for next in graph[now]:
                    if visited[next] == False:
                        visited[next] = True
                        queue.append(next)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N
    count = 0
    for i in range(N):
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    adj = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    visited = [False] * N
    count = 0
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in adj[v]:
                if visited[w]:
                    continue
                stack.append(w)
    print(count)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = [False] * N
    components = 0
    for i in range(N):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
        components += 1
    print(components)

main()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(n)
        return

    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, graph, visited)

    print(count)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    E = [list(map(int, input().split())) for i in range(M)]
    print(solve(N, M, E))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    graph = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
    visited = [False] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            ans += 1
            stack = [i]
            while stack:
                v = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                for w in graph[v]:
                    if not visited[w]:
                        stack.append(w)
    print(ans)

=======
Suggestion 10

def find_connected_components(n, edges):
    if not edges:
        return n
    visited = [False] * (n + 1)
    visited[0] = True
    connected_components = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        connected_components += 1
        stack = [i]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            for edge in edges:
                if edge[0] == node:
                    stack.append(edge[1])
                elif edge[1] == node:
                    stack.append(edge[0])
    return connected_components
