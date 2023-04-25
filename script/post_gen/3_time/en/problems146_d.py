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

    c = [0] * (N-1)
    color = 1
    for i in range(N):
        for j in G[i]:
            if c[j] == 0:
                c[j] = color
                color += 1

    print(max(c))
    for i in range(N-1):
        print(c[i])

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # coloring
    C = [0]*N
    for i in range(N):
        C[i] = len(set(C[j] for j in G[i])) + 1

    # output
    print(max(C))
    for i in range(N-1):
        print(C[i])

main()

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * (N-1)
    color = 1
    for v in range(N):
        used = [0] * (N+1)
        for u in G[v]:
            used[ans[u]] = 1
        for u in G[v]:
            if ans[u] == 0:
                for i in range(1, N+1):
                    if used[i] == 0:
                        ans[u] = i
                        used[i] = 1
                        break
    print(max(ans))
    for a in ans:
        print(a)
    return

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    from collections import deque
    Q = deque()
    Q.append(0)
    C = [-1]*N
    C[0] = 0
    while Q:
        v = Q.popleft()
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
    for c in C[1:]:
        print(c+1)

=======
Suggestion 5

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(N-1)
    for i in range(N-1):
        print(i)

=======
Suggestion 6

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]

    # 隣接リストを作成
    adjacent = [[] for _ in range(N+1)]
    for a, b in edges:
        adjacent[a].append(b)
        adjacent[b].append(a)

    # 各頂点の隣接頂点の色を格納
    colors = [[] for _ in range(N+1)]

    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        # 頂点vの隣接頂点を取得
        a = adjacent[v]
        # 頂点vの隣接頂点の色を格納
        colors[v] = c
        # 頂点vの隣接頂点をスタックに格納
        for i in a:
            stack.append(i)

    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        # 頂点vの隣接頂点を取得
        a = adjacent[v]
        # 頂点vの隣接頂点の色を格納
        colors[v] = c
        # 頂点vの隣接頂点をスタックに格納
        for i in a:
            stack.append(i)

    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        #

=======
Suggestion 7

def dfs(v, p):
  #print(v, p)
  c = 1
  for u in G[v]:
    if u == p:
      continue
    if c == color[v]:
      c += 1
    color[u] = c
    c += 1
    dfs(u, v)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
color = [-1] * N
color[0] = 1
dfs(0, -1)
print(max(color))
for i in range(N-1):
  print(color[i+1])

=======
Suggestion 8

def main():
    N = int(input())
    #print(N)
    #print("----")
    g = [[] for _ in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    #print(g)
    #print("----")
    c = [0]*(N-1)
    for i in range(N):
        color = 1
        for j in g[i]:
            if j < i:
                continue
            while color in g[i]:
                color += 1
            c[j] = color
            color += 1
    print(max(c))
    for i in range(N-1):
        print(c[i])

=======
Suggestion 9

def solve(n, edges):
    # i番目の頂点に隣接する頂点のリスト
    adj = [[] for _ in range(n)]
    # 1番目の頂点からの距離
    dist = [0] * n
    # 1番目の頂点からの距離をBFSで求める
    que = [0]
    while que:
        v = que.pop()
        for u in adj[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                que.append(u)
    # 頂点の距離が偶数ならば、その頂点から出る辺の色は0, 1, 2, ...と割り当てる
    # 頂点の距離が奇数ならば、その頂点から出る辺の色は1, 2, 3, ...と割り当てる
    # 割り当てられた色を出力する
    colors = [0] * (n - 1)
    for i, (v, u) in enumerate(edges):
        v -= 1
        u -= 1
        if dist[v] % 2 == 0:
            colors[i] = dist[u]
        else:
            colors[i] = dist[u] - 1
    return colors

=======
Suggestion 10

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]

    # 木の場合は、最大の隣接数+1が色の数になる
    max_adj = 0
    for i in range(n):
        adj = 0
        for j in range(n-1):
            if edges[j][0] == i+1 or edges[j][1] == i+1:
                adj += 1
        if max_adj < adj:
            max_adj = adj

    print(max_adj+1)
    for i in range(n-1):
        print(i%(max_adj+1)+1)

main()
