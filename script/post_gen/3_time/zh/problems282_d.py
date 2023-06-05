Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    edge.sort(key=lambda x: x[0])
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = 0
            for e in edge:
                if e[0] == i+1 and e[1] == j+1:
                    flag = 1
                    break
            if flag == 0:
                count += 1
    print(count)

=======
Suggestion 3

def solve():
    N,M = map(int,input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int,input().split())))
    edge.sort()
    ans = 0
    black = [0] * (N+1)
    white = [0] * (N+1)
    for i in range(M):
        u = edge[i][0]
        v = edge[i][1]
        if (black[u] == 0 and black[v] == 0) or (white[u] == 0 and white[v] == 0):
            ans += 1
            black[u] = 1
            black[v] = 1
        white[u] = 1
        white[v] = 1
    print(ans)
    return 0

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[1])
    cnt = 0
    for i in range(m):
        for j in range(i + 1, m):
            if edges[i][0] != edges[j][0] and edges[i][1] != edges[j][1]:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u-1].append(v-1)
        adj_list[v-1].append(u-1)

    for i in range(n):
        adj_list[i].sort()

    ans = 0
    for u, v in edges:
        if len(adj_list[u-1]) > len(adj_list[v-1]):
            u, v = v, u
        for w in adj_list[u-1]:
            if w in adj_list[v-1]:
                ans += 1
    print(ans)

solve()
