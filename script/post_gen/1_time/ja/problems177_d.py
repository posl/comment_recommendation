Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m=map(int,input().split())
    ab=[]
    for _ in range(m):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,m,ab

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    friends = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    groups = [set() for _ in range(n)]
    for i in range(n):
        if groups[i]:
            continue
        groups[i].add(i)
        for j in friends[i]:
            if groups[j]:
                continue
            groups[j] = groups[i]
    print(len(set(map(frozenset, groups))))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    group = [0] * N
    group_num = 0
    for i in range(N):
        if group[i] == 0:
            group_num += 1
            group[i] = group_num
            stack = [i]
            while stack:
                now = stack.pop()
                for j in friends[now]:
                    if group[j] == 0:
                        group[j] = group_num
                        stack.append(j)
    print(group_num)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    #print(friends)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        q = [i]
        while q:
            v = q.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in friends[v]:
                q.append(u)
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    f = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        f[a-1].add(b-1)
        f[b-1].add(a-1)

    ans = 0
    uf = UnionFind(n)
    for i in range(n):
        for j in f[i]:
            uf.union(i,j)
    ans = uf.size()
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    fri = [[] for i in range(N+1)]
    for i in range(M):
        A,B = map(int,input().split())
        fri[A].append(B)
        fri[B].append(A)
    ans = 0
    for i in range(1,N+1):
        if fri[i] != []:
            ans += 1
            for j in fri[i]:
                fri[j] = []
    print(ans)

main()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    uf = UnionFind(n)
    for a, b in edges:
        uf.unite(a - 1, b - 1)

    print(uf.group_count)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[0])
    ans = 1
    for i in range(M - 1):
        if AB[i][0] != AB[i + 1][0]:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #友達関係を表すグラフ
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
    #友達関係のグループ
    group = [-1] * N
    #グループの数
    group_num = 0
    #グループ分け
    for i in range(N):
        if group[i] != -1:
            continue
        #深さ優先探索
        stack = [i]
        while stack:
            v = stack.pop()
            group[v] = group_num
            for u in G[v]:
                if group[u] == -1:
                    stack.append(u)
        group_num += 1
    print(group_num)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    cnt = 0
    while AB:
        a, b = AB.pop(0)
        cnt += 1
        while AB:
            if AB[0][0] <= b:
                AB.pop(0)
            else:
                break
    print(cnt)
