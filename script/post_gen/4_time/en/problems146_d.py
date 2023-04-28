Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    C = [0]*N
    for i in range(N):
        C[i] = [0]*(len(G[i])+1)
    for i in range(N):
        for j in range(len(G[i])):
            C[i][j+1] = C[i][j] + 1
    for i in range(N):
        for j in range(len(G[i])):
            for k in range(j+1, len(G[i])):
                if C[G[i][j]][i+1] == C[G[i][k]][i+1]:
                    C[G[i][k]][i+1] += 1
    print(max(C[i]) + 1)
    for i in range(N):
        for j in range(len(G[i])):
            if i < G[i][j]:
                print(C[i][j+1])

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    #print(G)
    colors = [-1 for i in range(N)]
    colors[0] = 0
    stack = [0]
    while len(stack) > 0:
        v = stack.pop()
        c = 0
        for w in G[v]:
            if colors[w] == -1:
                while c == colors[v]:
                    c += 1
                colors[w] = c
                c += 1
                stack.append(w)
    print(max(colors)+1)
    for i in range(N-1):
        print(colors[i]+1)

=======
Suggestion 3

def main():
    N = int(input())
    tree = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    colors = [0] * N
    color = 1
    for i in range(N):
        used = set()
        for j in tree[i]:
            used.add(colors[j])
        for j in tree[i]:
            if colors[j] == 0:
                for k in range(1, N+1):
                    if k not in used:
                        colors[j] = k
                        used.add(k)
                        break
    print(max(colors))
    for i in colors:
        if i != 0:
            print(i)

=======
Suggestion 4

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    colors = [-1] * N
    colors[0] = 0
    for i in range(N):
        color = 0
        for j in adj[i]:
            if colors[j] == color:
                color += 1
        for j in adj[i]:
            if colors[j] == -1:
                colors[j] = color
                color += 1
    print(max(colors)+1)
    for i in range(N-1):
        print(colors[edges[i][0]-1]+1)

=======
Suggestion 5

def main():
    N = int(input())
    G = []
    for i in range(N-1):
        a, b = map(int, input().split())
        G.append([a,b])
    print(N-1)
    for i in range(N-1):
        print(i)

=======
Suggestion 6

def main():
    import sys
    from collections import defaultdict
    N = int(sys.stdin.readline())
    G = defaultdict(lambda: [])
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        G[a].append(b)
        G[b].append(a)
    #print(G)
    visited = [False] * (N+1)
    color = [0] * (N+1)
    def dfs(v, p, c):
        if visited[v]:
            return
        visited[v] = True
        color[v] = c
        for u in G[v]:
            if u == p:
                continue
            dfs(u, v, c+1)
    dfs(1, 0, 1)
    #print(color)
    print(max(color))
    for i in range(2, N+1):
        print(color[i])

main()

The only thing to note is that the sample output 2 and 3 is wrong. (The color of the edge from 2 to 4 should be 1, not 2.)

The following is a solution using the Union-Find data structure.

=======
Suggestion 7

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(edges)
    colors = [0] * (N-1)
    #print(colors)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[3][0])
    #print(edges[3][1])
    for i in range(N-1):
        if edges[i][0] == 1:
            colors[i] = edges[i][1]
        elif edges[i][1] == 1:
            colors[i] = edges[i][0]
    #print(colors)
    #print(colors[0])
    #print(colors[1])
    #print(colors[2])
    #print(colors[3])
    #print(colors[4])
    #print(colors[5])
    print(max(colors))
    for i in range(N-1):
        print(colors[i])

=======
Suggestion 8

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]

    # 木の辺の色を塗る
    # 隣接する頂点は同じ色にはできない
    # 隣接する頂点がすべて異なる色で塗られていれば、色の数は最小
    # 隣接する頂点が同じ色で塗られている場合、隣接する頂点の色を変える

    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    def get_adjacent_color(v, parent):
        adjacent_color = []
        for e in edges:
            if e[0] == v or e[1] == v:
                if e[0] == v:
                    adjacent_v = e[1]
                else:
                    adjacent_v = e[0]
                if adjacent_v != parent:
                    adjacent_color.append(color[e])
        return adjacent_color

    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    def get_color(v, parent):
        for i in range(1, N+1):
            if i not in get_adjacent_color(v, parent):
                return i

    # 木の辺を塗る
    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    color = [0] * (N-1)
    for i in range(N-1):
        color[i] = get_color(edges[i][0], edges[i][1])

    # 隣接する頂点の色を取得する
    # すでに塗られている

=======
Suggestion 9

def main():
    N = int(input())
    #各頂点の隣接頂点を格納するリスト
    node = [[] for _ in range(N+1)]
    #辺の色を格納するリスト
    color = [0 for _ in range(N)]
    for i in range(N-1):
        a,b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    #頂点の隣接頂点の色を格納するリスト
    color_node = [[] for _ in range(N+1)]
    #頂点1から順に隣接頂点の色を格納するリストに格納
    for i in range(N-1):
        for j in node[i+1]:
            color_node[i+1].append(color[j-1])
    #頂点の隣接頂点の色を格納するリストを走査し、頂点の隣接頂点の色が同じものがない色を辺の色として格納する
    for i in range(N-1):
        for j in range(1,N+1):
            if j not in color_node[i+1]:
                color[i] = j
                break
    #辺の色の最大値を出力
    print(max(color))
    #辺の色を出力
    for i in color:
        print(i)
