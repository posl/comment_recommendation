Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    for i in range(N):
        if len(G[i]) > 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if len(graph[1]) == 1 and len(graph[N]) == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            exit()
    print("Yes")
main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    e = [0 for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        e[a-1] += 1
        e[b-1] += 1
    for i in range(n):
        if e[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    visited = [False] * N
    def dfs(u, p):
        visited[u] = True
        for v in G[u]:
            if v == p:
                continue
            if visited[v]:
                return False
            if not dfs(v, u):
                return False
        return True
    if not dfs(0, -1):
        print('No')
        return
    if not all(visited):
        print('No')
        return
    print('Yes')
solve()

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n+1)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,n+1):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    if n == m+1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def path_graph():
    n,m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    edge.sort()
    for i in range(1, n):
        if [i, i+1] not in edge:
            return "No"
    return "Yes"
print(path_graph())
