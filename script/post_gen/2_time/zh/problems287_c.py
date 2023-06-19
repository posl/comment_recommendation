Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    return

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def get_graph():
    n,m = map(int,input().split())
    graph = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        u,v = map(int,input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    return graph

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    if n == 1:
        print('Yes')
        return
    if m == 0:
        print('No')
        return
    # 有m条边，n个点，m>=n-1
    if m < n-1:
        print('No')
        return
    # 有m条边，n个点，m<=n(n-1)/2
    if m > n*(n-1)/2:
        print('No')
        return
    # 有m条边，n个点，m>=n-1, m<=n(n-1)/2
    print('Yes')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1, N+1):
        if len(G[i]) > 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[0])
    for i in range(n - 1):
        if a[i][0] != a[i + 1][0] - 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort()
    print(edges)
    for i in range(M):
        if edges[i][0] == edges[i+1][0] or edges[i][1] == edges[i+1][1]:
            print("No")
            break
        else:
            print("Yes")
            break

=======
Suggestion 9

def isPathGraph(n, m, edges):
    if m != n-1:
        return False
    edges = sorted(edges, key=lambda x: x[0])
    for i in range(0, n-1):
        if edges[i][0] != i+1 or edges[i][1] != i+2:
            return False
    return True
