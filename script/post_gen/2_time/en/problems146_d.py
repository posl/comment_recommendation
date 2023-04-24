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

    C = [-1] * N
    C[0] = 0
    Q = [0]
    while Q:
        v = Q.pop()
        c = 0
        for w in G[v]:
            if C[w] != -1:
                continue
            while c == C[v]:
                c += 1
            C[w] = c
            c += 1
            Q.append(w)

    print(max(C)+1)
    for i in range(1, N):
        print(C[i]+1)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # DFSで頂点の深さを求める
    d = [-1] * N
    q = [0]
    d[0] = 0
    while q:
        v = q.pop()
        for nv in G[v]:
            if d[nv] != -1:
                continue
            d[nv] = d[v] + 1
            q.append(nv)

    # 深い頂点から順に色を割り当てる
    color = [-1] * N
    q = [N-1]
    color[N-1] = 0
    while q:
        v = q.pop()
        c = 0
        for nv in G[v]:
            if d[nv] <= d[v]:
                continue
            if c == color[v]:
                c += 1
            color[nv] = c
            c += 1
            q.append(nv)

    print(max(color) + 1)
    for i in range(N-1):
        print(color[i]+1)

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))
    C = [0] * (N-1)
    used = [0] * N
    Q = [0]
    while Q:
        v = Q.pop()
        c = 1
        for nv, i in G[v]:
            if C[i] != 0:
                continue
            if c == used[v]:
                c += 1
            C[i] = c
            used[nv] = c
            c += 1
            Q.append(nv)
    print(max(C))
    print('

'.join(map(str, C)))

main()

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        G[a].append((b, i))
        G[b].append((a, i))
    color = [-1] * (N-1)
    def dfs(v, p, c):
        k = 1
        for w, i in G[v]:
            if w == p: continue
            if k == c: k += 1
            color[i] = k
            dfs(w, v, k)
            k += 1
    dfs(0, -1, 0)
    print(max(color))
    for c in color:
        print(c)

=======
Suggestion 5

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    print(N - 1)
    for i in range(N - 1):
        print(i)

main()

=======
Suggestion 6

def main():
    N = int(input())
    edges = []
    for i in range(N - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    #print(edges)
    #print(N)

    #make a graph
    graph = [[] for i in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)

    #make a tree
    visited = [False] * (N + 1)
    visited[1] = True
    stack = [1]
    tree = [[] for i in range(N + 1)]
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                tree[v].append(i)
                stack.append(i)
                visited[i] = True
    #print(tree)

    #make a color
    color = [-1] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        c = 0
        for i in tree[v]:
            if c == color[v]:
                c += 1
            color[i] = c
            c += 1
            stack.append(i)
    #print(color)

    #print
    print(max(color))
    for i in range(N - 1):
        a, b = edges[i]
        if color[a] > color[b]:
            print(color[b] + 1)
        else:
            print(color[a] + 1)

=======
Suggestion 7

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    # グラフの隣接リストを作成
    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 頂点1から幅優先探索を行い、各頂点の深さを求める
    depth = [-1] * (N + 1)
    depth[1] = 0
    q = [1]
    while q:
        v = q.pop()
        for w in graph[v]:
            if depth[w] != -1:
                continue
            depth[w] = depth[v] + 1
            q.append(w)

    # 深さが奇数の頂点を赤、偶数の頂点を青とする
    colors = [''] * (N + 1)
    for i in range(1, N + 1):
        colors[i] = 'R' if depth[i] % 2 == 0 else 'B'

    # 各頂点の隣接頂点の色を取得
    adjacent_colors = []
    for a, b in edges:
        if colors[a] == 'R':
            adjacent_colors.append(colors[b])
        else:
            adjacent_colors.append(colors[a])

    # 隣接頂点の色の種類数を求める
    adjacent_colors = set(adjacent_colors)
    print(len(adjacent_colors))
    for color in colors[1:]:
        print(color)

=======
Suggestion 8

def main():
    N = int(input())
    # 1-indexed
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    # 1-indexed
    colors = [0] * (N+1)
    # 1-indexed
    used = [0] * (N+1)

    # 1-indexed
    for i in range(1, N+1):
        # 0-indexed
        for j in range(len(edges)):
            if i in edges[j]:
                # 1-indexed
                for k in range(1, N+1):
                    # 0-indexed
                    if k in edges[j]:
                        used[colors[k]] = 1
                # 0-indexed
                for k in range(1, N+1):
                    if used[k] == 0:
                        colors[i] = k
                        break
                # 0-indexed
                for k in range(1, N+1):
                    if k in edges[j]:
                        used[colors[k]] = 0

    print(max(colors))
    # 0-indexed
    for i in range(N-1):
        print(colors[edges[i][0]])

=======
Suggestion 9

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a,b = map(int,input().split())
        edges.append([a,b])

    #print(edges)

    #print("N",N)
    #print("edges",edges)

    #edges = [[1,2],[2,3],[2,4],[2,5],[4,7],[5,6],[6,8]]
    #edges = [[1,2],[2,3],[2,4],[2,5],[4,7],[5,6],[6,8]]
    colors = [0] * (N+1)
    color = 1
    for i in range(N-1):
        c = 1
        for j in range(2):
            if colors[edges[i][j]] == c:
                c += 1
        colors[edges[i][0]] = c
        colors[edges[i][1]] = c
        if color < c:
            color = c

    #print("colors",colors)

    print(color)
    for i in range(N-1):
        print(colors[edges[i][0]])

=======
Suggestion 10

def main():
    #N is the number of vertices
    N = int(input())
    #adjacency list
    adj = [[] for _ in range(N)]
    #colors
    colors = [0] * N
    #for each vertex
    for i in range(N-1):
        #a_i and b_i are two vertices that are connected by an edge
        a_i, b_i = map(int, input().split())
        #append b_i to adjacency list of a_i
        adj[a_i-1].append(b_i-1)
        #append a_i to adjacency list of b_i
        adj[b_i-1].append(a_i-1)

    #queue
    q = [0]
    #for each vertex
    for i in range(N):
        #color of i-th vertex
        color = 1
        #for each vertex j that is connected to i-th vertex
        for j in adj[i]:
            #if j-th vertex is already colored
            if colors[j] != 0:
                #if the color of j-th vertex is equal to the current color
                if colors[j] == color:
                    #increment the current color
                    color += 1
        #color the i-th vertex
        colors[i] = color
        #for each vertex j that is connected to i-th vertex
        for j in adj[i]:
            #if j-th vertex is not colored
            if colors[j] == 0:
                #append j-th vertex to the queue
                q.append(j)
    #print the number of colors used
    print(max(colors))
    #for each vertex
    for i in range(N-1):
        #print the color of the i-th edge
        print(colors[i])
