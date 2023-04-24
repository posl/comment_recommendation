Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N - len(set(A + B)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    a = [x - 1 for x in a]
    b = [x - 1 for x in b]

    # 各ノードの親を記録する
    # つまり、各ノードの根を記録する
    parent = [-1] * N

    # ノードxの根を求める
    def root(x):
        # ノードxの親が存在しない場合は、xが根である
        if parent[x] < 0:
            return x
        # ノードxの親が存在する場合は、親の根を求める
        else:
            # 根を求めると同時に、xの親を根につなぎ直す
            parent[x] = root(parent[x])
            return parent[x]

    # ノードxとノードyの属する集合を併合する
    def unite(x, y):
        # ノードxとノードyの根を求める
        x = root(x)
        y = root(y)

        # ノードxとノードyの根が同じ場合は、何もしない
        if x == y:
            return
        # ノードxの根の方がノードyの根よりも大きい場合は、xとyを入れ替える
        if parent[x] > parent[y]:
            x, y = y, x

        # ノードxの根の子供にノードyの根を追加する
        parent[x] += parent[y]
        parent[y] = x

    # ノードxとノードyが同じ集合に属するかどうかを判定する
    def same(x, y):
        return root(x) == root(y)

    #

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
    ans = 0
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in G[v]:
                if visited[u]:
                    continue
                stack.append(u)
    print(ans)

main()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    friends = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)
    groups = [None] * n
    group_count = 0
    for i in range(n):
        if groups[i] is not None:
            continue
        groups[i] = group_count
        stack = [i]
        while stack:
            p = stack.pop()
            for q in friends[p]:
                if groups[q] is None:
                    groups[q] = group_count
                    stack.append(q)
        group_count += 1
    print(group_count)

main()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in edges[v]:
                if not visited[u]:
                    stack.append(u)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    #print(E)

    visited = [0]*N
    group = 0
    for i in range(N):
        if visited[i] == 0:
            group += 1
            visited[i] = group
            stack = [i]
            while stack:
                v = stack.pop()
                for w in E[v]:
                    if visited[w] == 0:
                        visited[w] = group
                        stack.append(w)
    print(group)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i]-1,b[i]-1)
    ans = 0
    for i in range(n):
        if uf.find(i) == i:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    uf = UnionFind(n)
    for _ in range(m):
        a,b = map(int,input().split())
        uf.union(a-1,b-1)
    print(uf.group_num-1)

=======
Suggestion 9

def main():
    n,m=map(int,input().split())
    e=[[] for i in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    def dfs(v):
        if v in s:
            return
        s.add(v)
        for u in e[v]:
            dfs(u)
    s=set()
    cnt=0
    for i in range(n):
        if i not in s:
            dfs(i)
            cnt+=1
    print(cnt)

main()

You can find the problem here.

I am a beginner in competitive programming. I am trying to solve this problem. I am using python. I have written the following code. But I am getting wrong answer. Can you please tell me where I am going wrong?

=======
Suggestion 10

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
