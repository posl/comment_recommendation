Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = 1
        else:
            d[u] += 1
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    for v in d:
        if d[v] > 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = set()
        if v not in d:
            d[v] = set()
        d[u].add(v)
        d[v].add(u)

    if len(d[1]) != 1 or len(d[n]) != 1:
        print('No')
    else:
        for i in range(2, n):
            if len(d[i]) != 2:
                print('No')
                return
        print('Yes')

=======
Suggestion 4

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
    for u in range(N):
        if len(G[u]) > 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    if N == M + 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[0])
    if edges[0][0] != 1 or edges[-1][1] != n:
        print("No")
        return
    for i in range(1, m):
        if edges[i][0] != edges[i-1][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[0])
    if edges[0][0] == 1:
        for i in range(M-1):
            if edges[i][1] != edges[i+1][0]:
                print("No")
                exit()
        print("Yes")
    elif edges[-1][1] == N:
        for i in range(M-1):
            if edges[i][1] != edges[i+1][0]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    #import sys
    #input = sys.stdin.readline
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    E = [list(map(int, input().split())) for _ in range(M)]
    E.sort()
    for i in range(M):
        if E[i][0] != i + 1:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 9

def check_path_graph(n, m, edges):
    if m != n - 1:
        return 'No'
    else:
        for i in range(n):
            if len(edges[i]) != 2:
                return 'No'
        return 'Yes'

=======
Suggestion 10

def is_path_graph(n,m,edges):
    if m != n - 1:
        return False
    if max(edges) != n or min(edges) != 1:
        return False
    if len(set(edges)) != n-1:
        return False
    return True
