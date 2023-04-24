Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    P = list(map(int, input().split()))
    for i in range(8):
        P[i] -= 1
    P.insert(0, -1)
    P.append(-1)
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if j in G[i]:
                G[i].remove(j)
            else:
                G[i].append(j)
    for i in range(9):
        G[i] = sorted(G[i])
    def dfs(v, p, d, used):
        if v == 8:
            if d == 0:
                return 0
            else:
                return 10**9
        if d == 0:
            return 10**9
        if used[v]:
            return 10**9
        res = 10**9
        used[v] = True
        for u in G[p[v]]:
            res = min(res, dfs(v+1, p, d-1, used))
        used[v] = False
        res = min(res, dfs(v+1, p, d, used))
        return res
    res = dfs(0, P, 16, [False]*9)
    print(-1 if res == 10**9 else res)

=======
Suggestion 2

def main():
    M = int(input())
    graph = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    pos = list(map(int, input().split()))
    pos = [p-1 for p in pos]
    empty = 8
    for p in pos:
        if p == 8:
            empty = 8
            break
    for i in range(9):
        if i in pos:
            continue
        empty = i
        break
    graph[empty].append(empty)
    graph[empty].sort()

    def dfs(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs(u, visited)

    visited = set()
    dfs(empty, visited)
    if len(visited) != 9:
        print(-1)
        return

    def dfs2(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs2(u, visited)

    visited = set()
    dfs2(pos[0], visited)
    if len(visited) != 9:
        print(-1)
        return

    def dfs3(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs3(u, visited)

    visited = set()
    dfs3(pos[1], visited)
    if len(visited) != 9:
        print(-1)
        return

    def bfs(v, visited):
        q = [v]
        while q:
            v = q.pop()
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    q.append(u)

    visited = set()
    bfs(empty, visited)
    if len(visited) != 9:
        print(-1)
        return

    def bfs2(v, visited):
        q = [v]
        while q:
            v = q.pop()
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    q.append(u)

    visited = set()
    bfs2(pos[0], visited)
    if len(visited) != 9:
        print(-1)
        return

=======
Suggestion 3

def main():
    M = int(input())
    graph = [[0] * 9 for i in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    pieces = list(map(int, input().split()))
    pieces = [p - 1 for p in pieces]
    pieces = [pieces.inde

=======
Suggestion 4

def main():
    M = int(input())
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    pieces = list(map(int, input().split()))

    # 1. 1つの連結成分になっているか
    # 2. 1つの連結成分になっているなら、それが8つの頂点を持つか
    # 3. 8つの頂点を持つなら、それが8つのピースを持つか

    # 1. 1つの連結成分になっているか
    # 1-1. 連結成分を求める
    # 1-2. 連結成分が1つであるか
    # 1-3. 連結成分が8つの頂点を持つか
    # 1-4. 連結成分が8つのピースを持つか

    # 1-1. 連結成分を求める
    # 1-1-1. 連結成分を求める
    # 1-1-2. 連結成分を求める
    # 1-1-3. 連結成分を求める
    # 1-1-4. 連結成分を求める

    # 1-1-1. 連結成分を求める
    # 1-1-1-1. 連結成分を求める
    # 1-1-1-2. 連結成分を求める
    # 1-1-1-3. 連結成分を求める
    # 1-1-1-4. 連結成分を求める

    # 1-1-1-1. 連結成分を求める
    # 1-1-1-1-1. 連結成分を求める
    #

=======
Suggestion 5

def main():
    import sys
    from collections import deque

    def input():
        return sys.stdin.readline()[:-1]

    M = int(input())
    graph = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    pieces = list(map(int, input().split()))
    for i in range(8):
        pieces[i] -= 1
    empty = 8
    for i in range(9):
        if i not in pieces:
            empty = i
            break

    def bfs(start, goal):
        queue = deque()
        queue.append(start)
        visited = [False] * 9
        visited[start] = True
        while queue:
            now = queue.popleft()
            if now == goal:
                return True
            for next in graph[now]:
                if visited[next]:
                    continue
                visited[next] = True
                queue.append(next)
        return False

    def dfs(now, visited, count):
        if count == 8:
            return True
        for next in range(9):
            if next in visited:
                continue
            if next == empty:
                continue
            if next not in graph[now]:
                continue
            visited.add(next)
            if dfs(next, visited, count + 1):
                return True
            visited.remove(next)
        return False

    for i in range(8):
        if not bfs(pieces[i], i):
            print(-1)
            return
        if not bfs(empty, pieces[i]):
            print(-1)
            return
    for i in range(8):
        if not bfs(pieces[i], empty):
            print(-1)
            return
    for i in range(8):
        if not bfs(pieces[i], pieces[(i + 1) % 8]):
            print(-1)
            return
    if dfs(empty, set(), 0):
        print(0)
        return
    print(8)

=======
Suggestion 6

def main():
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    #print(edges)
    #print(pieces)
    #print(M)

    # 1. 8つのピースが全て隣り合うように移動する
    # 2. 1つのピースを移動する
    # 3. 1つのピースを移動する
    # 4. 1つのピースを移動する
    # 5. 1つのピースを移動する
    # 6. 1つのピースを移動する
    # 7. 1つのピースを移動する
    # 8. 1つのピースを移動する
    # 9. 1つのピースを移動する
    # 10. 1つのピースを移動する
    # 11. 1つのピースを移動する
    # 12. 1つのピースを移動する
    # 13. 1つのピースを移動する
    # 14. 1つのピースを移動する
    # 15. 1つのピースを移動する
    # 16. 1つのピースを移動する
    # 17. 1つのピースを移動する
    # 18. 1つのピースを移動する
    # 19. 1つのピースを移動する
    # 20. 1つのピースを移動する
    # 21. 1つのピースを移動する
    # 22. 1つのピースを移動する
    # 23. 1つのピースを移動する
    # 24. 1つのピースを移動する
    # 25. 1つのピースを移動する
    # 26. 1つのピースを移動する
    # 27. 1つのピースを移動する
    # 28.

=======
Suggestion 7

def solve():
    from collections import defaultdict
    from queue import Queue
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, 10):
        graph[i].append(i)
    # print(graph)
    # 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8
    # 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8
    # 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 0
    # 0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 0
    # 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 0, 9: 1
    # 0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 0, 8: 1
    # 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 0, 8: 1, 9: 2
    # 0: 3,

=======
Suggestion 8

def main():
    import sys
    from collections import deque
    M = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    p = tuple(map(int, input().split()))
    # 隣接リストを作る
    adj = [[] for _ in range(10)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # 1から8の頂点について、p[i]からiへの移動を考える
    # 1から8の頂点について、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空

=======
Suggestion 9

def main():
    M = int(input())
    edge = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))

    # 0: empty, 1: piece1, 2: piece2, ..., 9: piece9
    p.insert(0, 0)
    p = [i - 1 for i in p]

    # adj[v]: vertices adjacent to v
    adj = [[] for _ in range(9)]
    for u, v in edge:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # dist[v][i]: minimum number of operations to move piece i to vertex v
    dist = [[float("inf")] * 9 for _ in range(9)]
    for v in range(9):
        dist[v][p[v]] = 0

    # bfs
    q = []
    for v in range(9):
        q.append((v, p[v]))
    while q:
        v, i = q.pop(0)
        for u in adj[v]:
            if dist[u][i] == float("inf"):
                dist[u][i] = dist[v][i] + 1
                q.append((u, i))

    # dp[s][i]: minimum number of operations to move pieces in state s to vertices i, j, k, ..., p[s]
    dp = [[float("inf")] * 9 for _ in range(1 << 8)]
    dp[0][0] = 0
    for s in range(1 << 8):
        for v in range(9):
            for i in range(8):
                if (s >> i) & 1 == 0:
                    s2 = s | (1 << i)
                    dp[s2][p[i]] = min(dp[s2][p[i]], dp[s][v] + dist[v][i])

    ans = min(dp[-1])
    print(ans if ans != float("inf") else -1)

=======
Suggestion 10

def find_empty_vertex ( graph ) : 
     for   i   in   range ( 9 ) : 
         if   i   not   in   graph : 
             return   i 

 def   find_adjacent_vertices ( graph ,   vertex ) : 
     return   [ v   for   v   in   graph [ vertex ]   if   v   in   graph ] 

 def   find_adjacent_pieces ( graph ,   pieces ,   vertex ) : 
     return   [ pieces [ v ]   for   v   in   graph [ vertex ]   if   v   in   graph ] 

 def   find_piece ( pieces ,   vertex ) : 
     return   pieces . index ( vertex ) 

 def   find_empty_piece ( pieces ) : 
     return   pieces . index ( - 1 ) 

 def   is_complete ( pieces ) : 
     return   all ( [ pieces [ i ]   ==   i   for   i   in   range ( 8 ) ] ) 

 def   solve ( graph ,   pieces ,   num_operations ) : 
     if   is_complete ( pieces ) : 
         return   num_operations 

     empty_vertex   =   find_empty_vertex ( graph ) 
     adjacent_vertices   =   find_adjacent_vertices ( graph ,   empty_vertex ) 
     adjacent_pieces   =   find_adjacent_pieces ( graph ,   pieces ,   empty_vertex ) 
     empty_piece   =   find_empty_piece ( pieces ) 

     for   ( vertex ,   piece )   in   zip ( adjacent_vertices ,   adjacent_pieces ) : 
         pieces [ empty_piece ]   =   vertex 
         pieces [ piece ]   =   - 1 
         del   graph [ empty_vertex ] 
         graph [ vertex ]   =   [ edge   for   edge   in   graph [ vertex ]   if   edge   !=   empty_vertex ] 
         num_operations   +=   1 
         ret   =   solve ( graph ,   pieces ,   num_operations ) 
         if   ret   !=   - 1 : 
             return   ret 
         pieces [ empty_piece ]   =   - 1 
         pieces [ piece ]   =   vertex 
         graph [ vertex ]   =   adjacent_vertices 
         graph [ empty_vertex ]   =   [ edge   for   edge   in   graph [ empty_vertex ]   if   edge   !=   vertex ]
