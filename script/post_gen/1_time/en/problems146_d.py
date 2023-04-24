Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    color = [0] * (N-1)
    used = [0] * (N+1)
    k = 0
    for v in range(N):
        c = 1
        for u in G[v]:
            if u < v:
                continue
            while used[c]:
                c += 1
            used[c] = 1
            color[u-1] = c
            k = max(k, c)
            c += 1
        for u in G[v]:
            if u < v:
                continue
            used[color[u-1]] = 0

    print(k)
    for c in color:
        print(c)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # 木の直径を求める
    # 0番目の頂点から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    v = 0
    maxd = 0
    for i in range(N):
        d = dfs(i, -1)
        if d > maxd:
            maxd = d
            v = i

    # 0番目の頂点から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd = dfs(v, -1)

    # 木の直径の中心から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd //= 2
    for _ in range(maxd):
        for i in range(N):
            if len(G[i]) == 1:
                G[G[i][0]].remove(i)
                G[i] = []
                break

    # 木の直径の中心から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd = dfs(v, -1)

    # 木の直径の中心から最も遠い頂点を求める

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    color = [-1]*N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        c = 0
        for u in G[v]:
            if color[u] != -1:
                continue
            while c == color[v] or c == color[G[v][G[v].index(u)-1]]:
                c += 1
            color[u] = c
            c += 1
            stack.append(u)
    print(max(color)+1)
    for i in range(N-1):
        print(color[i]+1)

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    print(N-1)
    for i in range(1,N+1):
        for j in G[i]:
            if i < j:
                print(G[i].index(j))

=======
Suggestion 5

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(i)
        G[b-1].append(i)
    K = 0
    for i in range(N):
        K = max(K, len(G[i]))
    print(K)
    for i in range(N):
        for j in range(len(G[i])):
            print(j+1)

=======
Suggestion 6

def main():
    N = int(input())
    E = [[int(x) for x in input().split()] for _ in range(N-1)]
    G = [[] for _ in range(N+1)]
    for a,b in E:
        G[a].append(b)
        G[b].append(a)
    C = [0] * (N+1)
    def dfs(v, p):
        c = 1
        for u in G[v]:
            if u == p: continue
            if c == C[v]: c += 1
            C[u] = c
            c += 1
            dfs(u, v)
    dfs(1, 0)
    print(max(C))
    for a,b in E:
        if C[a] < C[b]: a,b = b,a
        print(C[a])

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    print(n-1)
    for a, b in edges:
        print(min(a, b))

=======
Suggestion 8

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N)
    #print(edges)
    colors = [0] * (N-1)
    #print(colors)
    for i in range(N-1):
        #print(i)
        #print(edges[i])
        #print(edges[i][0])
        #print(edges[i][1])
        #print(colors)
        if colors[edges[i][0]-1] == 0:
            colors[edges[i][0]-1] = 1
        if colors[edges[i][1]-1] == 0:
            colors[edges[i][1]-1] = 1
        if colors[edges[i][0]-1] == colors[edges[i][1]-1]:
            colors[edges[i][1]-1] += 1
    #print(colors)
    print(max(colors))
    for i in range(N-1):
        print(colors[i])

=======
Suggestion 9

def main():
    N = int(input())
    edges = [list(map(int,input().split())) for _ in range(N-1)]
    edge_color = [0]*(N-1)
    color = [0]*(N+1)
    for i in range(N-1):
        a,b = edges[i]
        if color[a] == color[b]:
            edge_color[i] = 1
        else:
            edge_color[i] = min(color[a],color[b])
        color[a] = color[b] = edge_color[i] + 1
    print(max(edge_color))
    for c in edge_color:
        print(c)

=======
Suggestion 10

def main():
  N = int(input())
  #a,b = map(int,input().split())
  #A = list(map(int,input().split()))
  #S = input()
  #S = [input() for _ in range(H)]
  #S = [list(input()) for _ in range(H)]
  #S = [int(input()) for _ in range(N)]
  #S = [list(map(int,input().split())) for _ in range(N)]
  #S = [input().split() for _ in range(N)]
  #S = [list(map(int,input().split())) for _ in range(N)]
  #T = [int(input()) for _ in range(M)]
  #T = [list(map(int,input().split())) for _ in range(M)]
  #T = [input().split() for _ in range(M)]
  #T = [list(map(int,input().split())) for _ in range(M)]
  #G = [[] for _ in range(N)]
  G = [0]*(N+1)
  for _ in range(N-1):
    a,b = map(int,input().split())
    G[a] += 1
    G[b] += 1
  print(max(G))
  for i in range(1,N):
    print(i)

main()
