Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])

    # 木の直径
    def bfs(s):
        d = [-1] * (N+1)
        q = [s]
        d[s] = 0
        while q:
            v = q.pop()
            for nv in G[v]:
                if d[nv] == -1:
                    d[nv] = d[v] + 1
                    q.append(nv)
        return d

    d = bfs(1)
    # 頂点1から最も遠い頂点を求める
    farthest = 1
    for i in range(1, N+1):
        if d[i] > d[farthest]:
            farthest = i
    # 頂点farthestから最も遠い頂点を求める
    d = bfs(farthest)
    farthest = 1
    for i in range(1, N+1):
        if d[i] > d[farthest]:
            farthest = i
    # farthestから頂点1への経路を求める
    path = []
    v = farthest
    while v != 1:
        for nv in G[v]:
            if d[nv] + 1 == d[v]:
                path.append(nv)
                v = nv
                break

    # 答えを求める
    ans = [0] * (N+1)
    for i in range(len(path)-1):
        ans[path[i]] = path[i+1]
    ans[path[-1]] = 1

    print('Yes')
    for i in range(2, N+1):
        print(ans[i])

main()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    prev = [-1] * n
    queue = [0]
    while queue:
        current = queue.pop()
        for neighbor in graph[current]:
            if prev[neighbor] == -1:
                prev[neighbor] = current
                queue.append(neighbor)
    if -1 in prev[1:]:
        print('No')
    else:
        print('Yes')
        for i in prev[1:]:
            print(i+1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0]*(N+1)
    ans[1] = 1
    for i in range(M):
        if ans[A[i]] != 0:
            ans[B[i]] = A[i]
        elif ans[B[i]] != 0:
            ans[A[i]] = B[i]
    if 0 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for i in range(2, N+1):
            print(ans[i])

=======
Suggestion 4

def   main (): 
     N ,   M   =   map ( int ,   input (). split ()) 
     G   =   [[]   for   _   in   range ( N + 1 )] 
     for   _   in   range ( M ): 
         a ,   b   =   map ( int ,   input (). split ()) 
         G [ a ]. append ( b ) 
         G [ b ]. append ( a ) 
     dist   =   [- 1 ]   *   ( N + 1 ) 
     dist [ 1 ]   =   0 
     q   =   [ 1 ] 
     while   q : 
         v   =   q . pop () 
         for   nv   in   G [ v ]: 
             if   dist [ nv ]   !=   - 1 : 
                 continue 
             dist [ nv ]   =   dist [ v ]   +   1 
             q . append ( nv ) 
     if   - 1   in   dist [ 2 :]: 
         print ( "No" ) 
     else : 
         print ( "Yes" ) 
         for   i   in   range ( 2 ,   N + 1 ): 
             for   nv   in   G [ i ]: 
                 if   dist [ i ]   ==   dist [ nv ]   +   1 : 
                     print ( nv ) 
                     break

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    par = [-1]*N
    par[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if par[nv] == -1:
                par[nv] = v
                stack.append(nv)

    print('Yes')
    for p in par[1:]:
        print(p+1)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    if M % 2 == 1:
        print("No")
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    print("Yes")
    print(*[b + 1 for b in G[0]], sep = "

")
    return

=======
Suggestion 7

def main():
    # Read data
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # Create graph
    graph = [[] for _ in range(N+1)]
    for A, B in AB:
        graph[A].append(B)
        graph[B].append(A)

    # Create tree
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in graph[i]:
            if j != 1:
                tree[i].append(j)

    # Find the shortest path
    visited = [False] * (N+1)
    visited[1] = True
    queue = [(1, 1)]
    while queue:
        v, p = queue.pop(0)
        if v == 1:
            continue
        for w in tree[v]:
            if visited[w]:
                continue
            visited[w] = True
            queue.append((w, v))

    # Output
    print("Yes")
    for i in range(2, N+1):
        print(p)

=======
Suggestion 8

def main():
    # taking input
    n, m = map(int, input().split())
    # making the graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # making the tree
    tree = [0] * n
    tree[0] = -1
    q = [0]
    while q:
        node = q.pop()
        for child in graph[node]:
            if tree[child] == 0:
                tree[child] = node + 1
                q.append(child)
    # checking if the tree is valid
    for i in range(1, n):
        if tree[i] == 0:
            print('No')
            return
    # printing the tree
    print('Yes')
    for i in range(1, n):
        print(tree[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]

    # 1からNまでのループ
    for i in range(1, N + 1):
        # 1からNまでのループ
        for j in range(1, N + 1):
            # 1からNまでのループ
            for k in range(1, N + 1):
                # iからjまでのループ
                for l in range(1, N + 1):
                    # iからjまでのループ
                    for m in range(1, N + 1):
                        # iからjまでのループ
                        for n in range(1, N + 1):
                            # iからjまでのループ
                            for o in range(1, N + 1):
                                # iからjまでのループ
                                for p in range(1, N + 1):
                                    # iからjまでのループ
                                    for q in range(1, N + 1):
                                        # iからjまでのループ
                                        for r in range(1, N + 1):
                                            # iからjまでのループ
                                            for s in range(1, N + 1):
                                                # iからjまでのループ
                                                for t in range(1, N + 1):
                                                    # iからjまでのループ
                                                    for u in range(1, N + 1):
                                                        # iからjまでのループ
                                                        for v in range(1, N + 1):
                                                            # iからjまでのループ
                                                            for w in range(1, N + 1):
                                                                # iからjまでのループ
                                                                for x in range(1, N + 1):
                                                                    # iからjまでのループ
                                                                    for y in range(1, N + 1):
                                                                        # iからjまでのループ
                                                                        for z in range(1, N + 1):
                                                                            # iからjまでのループ
                                                                            for a

=======
Suggestion 10

def   solve ( N ,   M ,   AB ): 
     # 1. 連結成分分解 
     # 2. 各連結成分について、親の情報を持つ 
     # 3. 連結成分の中で、ループがあるかどうかを判定 
     # 4. ループがある場合は、ループの中で最も深いノードをループの親とする 
     # 5. ループがない場合は、深さが最も深いノードを親とする 
     # 6. 親の情報を元に、ループの親を辿っていくことで、ループの各ノードに対する親を求める 
     # 7. 親の情報を元に、ループの親を辿っていくことで、ループの各ノードに対する親を求める 
     # 8. それぞれのノードに対して、親の情報を用いて、ループの親を辿っていくことで、ループを出るまでの深さを求める 
     # 9. それぞれのノードに対して、ループを出るまでの深さを用いて、ループの親を辿っていくことで、ループの親を求める 
     # 10. それぞれのノードに対して、ループの親を求めることで、ループの各ノードに対する親を求める 
     # 11. それぞれのノードに対して、ループの各ノードに対する親を求めることで、ループの各ノードに対する親を求める 
     #
