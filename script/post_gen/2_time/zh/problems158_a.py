Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    # 友達関係を表すグラフを作成する
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    # ブロック関係を表すグラフを作成する
    B = [[] for _ in range(N)]
    for c, d in CD:
        B[c - 1].append(d - 1)
        B[d - 1].append(c - 1)

    # 幅優先探索を行う
    # 頂点sから各頂点への最短距離を求める
    def bfs(s, G):
        dist = [-1] * N
        que = []
        dist[s] = 0
        que.append(s)
        while que:
            v = que.pop(0)
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    que.append(nv)
        return dist

    # 頂点0を始点とした時の最短距離を求める
    dist = bfs(0, G)

    # 頂点0から各頂点への最短距離が2以下であれば、
    # 友達候補となる頂点である
    ans = [0] * N
    for i in range(N):
        if dist[i] <= 2:
            ans[i] = 1

    # 頂点0から各頂点への最短距離が2以下である頂点を
    # 頂点とするグラフを作成する
    G2 = [[] for _ in range(N)]
    for i in range(N):

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def bfs(start, end, graph):
    visited = [0] * (len(graph) + 1)
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
    return False

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    l = []
    for i in range(m):
        l.append(list(map(int,input().split())))
    l2 = []
    for i in range(k):
        l2.append(list(map(int,input().split())))
    l3 = []
    for i in range(n):
        l3.append(0)
    for i in range(m):
        l3[l[i][0]-1] += 1
        l3[l[i][1]-1] += 1
    for i in range(k):
        l3[l2[i][0]-1] -= 1
        l3[l2[i][1]-1] -= 1
    for i in range(n):
        l3[i] -= 1
    for i in range(n):
        print(l3[i],end=" ")

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A-1].append(B-1)
        friends[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C-1].append(D-1)
        blocks[D-1].append(C-1)
    for i in range(N):
        ans = len(friends[i])
        for j in blocks[i]:
            if j in friends[i]:
                ans -= 1
        for j in friends[i]:
            for k in friends[j]:
                if k != i and k not in friends[i] and k not in blocks[i]:
                    ans += 1
        print(ans, end=" ")
    print()

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    for i in range(K):
        blocks.append(list(map(int, input().split())))

    #print(N, M, K)
    #print(friends)
    #print(blocks)

    candidates = [0] * N
    for i in range(N):
        for j in range(M):
            if friends[j][0] == i + 1:
                candidates[i] += 1
            if friends[j][1] == i + 1:
                candidates[i] += 1

    #print(candidates)

    for i in range(N):
        for j in range(K):
            if blocks[j][0] == i + 1:
                candidates[i] -= 1
            if blocks[j][1] == i + 1:
                candidates[i] -= 1

    #print(candidates)

    for i in range(N):
        for j in range(M):
            if friends[j][0] == i + 1:
                candidates[i] -= 1
            if friends[j][1] == i + 1:
                candidates[i] -= 1

    #print(candidates)

    for i in range(N):
        for j in range(K):
            if blocks[j][0] == i + 1:
                candidates[i] += 1
            if blocks[j][1] == i + 1:
                candidates[i] += 1

    #print(candidates)

    for i in range(N):
        print(candidates[i], end=' ')

main()
