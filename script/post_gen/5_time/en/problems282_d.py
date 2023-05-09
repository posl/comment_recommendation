Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    color = [None] * N
    def dfs(v, c):
        if color[v] is not None:
            return color[v] == c
        color[v] = c
        for w in G[v]:
            if not dfs(w, 1-c):
                return False
        return True

    ans = 0
    for v in range(N):
        if color[v] is None:
            if dfs(v, 0):
                cnt0 = color.count(0)
                cnt1 = N - cnt0
                ans += cnt0 * (cnt0-1) // 2 + cnt1 * (cnt1-1) // 2
            else:
                ans += N * (N-1) // 2
    print(ans)

solve()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [-1] * N
    def dfs(v, c):
        visited[v] = c
        for nv in graph[v]:
            if visited[nv] == c:
                return False
            if visited[nv] == -1 and not dfs(nv, 1-c):
                return False
        return True
    ans = 0
    for i in range(N):
        if visited[i] == -1:
            if dfs(i, 0):
                n0 = visited.count(0)
                n1 = visited.count(1)
                ans += n0 * n1
            else:
                ans = -1
                break
    print(ans)

=======
Suggestion 3

def dfs(v, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == c:
            return False
        if color[g[v][i]] == 0 and not dfs(g[v][i], -c):
            return False
    return True

N, M = map(int, input().split())
g = [[] for i in range(N)]
color = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans * (N - ans) - M)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort(key=lambda x: x[0])

    ans = 0
    cur = 0
    for i in range(1, n + 1):
        if edges[cur][0] == i:
            cur += 1
        else:
            ans += n - i
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    adj = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * n
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == c:
                return False
            if color[v] == -1 and not dfs(v, 1 - c):
                return False
        return True
    ans = 0
    for u in range(n):
        if color[u] != -1:
            continue
        if not dfs(u, 0):
            print(0)
            return
        ans += 1
    print(ans * (n - ans) - m)
main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[1])
    edges.sort(key=lambda x: x[0])
    print(edges)
    #for i in range(m):
    #    for j in range(i+1, m):
    #        if edges[i][0] < edges[j][0] and edges[i][1] < edges[j][1]:
    #            pass
    #        else:
    #            if edges[i][1] < edges[j][0]:
    #                print(edges[i], edges[j])
    #                ans += 1
    #            elif edges[i][0] > edges[j][1]:
    #                print(edges[i], edges[j])
    #                ans += 1
    #print(ans)

=======
Suggestion 7

def main():
    #N = 5
    #M = 4
    #u = [4, 3, 5, 3]
    #v = [2, 1, 2, 2]

    N = 9
    M = 11
    u = [4, 9, 8, 8, 9, 8, 6, 4, 7, 4, 7]
    v = [9, 1, 2, 3, 2, 4, 7, 6, 5, 5, 8]

    #N = 4
    #M = 3
    #u = [3, 3, 1]
    #v = [1, 2, 2]

    #N = 5
    #M = 4
    #u = [4, 3, 5, 3]
    #v = [2, 1, 2, 2]

    #N = 9
    #M = 11
    #u = [4, 9, 8, 8, 9, 8, 6, 4, 7, 4, 7]
    #v = [9, 1, 2, 3, 2, 4, 7, 6, 5, 5, 8]

    #N = 5
    #M = 4
    #u = [4, 3, 5, 3]
    #v = [2, 1, 2, 2]

    #N = 9
    #M = 11
    #u = [4, 9, 8, 8, 9, 8, 6, 4, 7, 4, 7]
    #v = [9, 1, 2, 3, 2, 4, 7, 6, 5, 5, 8]

    #N = 5
    #M = 4
    #u = [4, 3, 5, 3]
    #v = [2, 1, 2, 2]

    #N = 9
    #M = 11

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges = sorted(edges, key=lambda x: x[0])
    #print(edges)
    #print(N, M)
    #print(edges)
    #print(edges[0][0], edges[0][1])
    #print(edges[1][0], edges[1][1])
    #print(edges[2][0], edges[2][1])
    #print(edges[3][0], edges[3][1])
    #print(edges[4][0], edges[4][1])
    #print(edges[5][0], edges[5][1])
    #print(edges[6][0], edges[6][1])
    #print(edges[7][0], edges[7][1])
    #print(edges[8][0], edges[8][1])
    #print(edges[9][0], edges[9][1])
    #print(edges[10][0], edges[10][1])
    #print(edges[11][0], edges[11][1])
    #print(edges[12][0], edges[12][1])
    #print(edges[13][0], edges[13][1])
    #print(edges[14][0], edges[14][1])
    #print(edges[15][0], edges[15][1])
    #print(edges[16][0], edges[16][1])
    #print(edges[17][0], edges[17][1])
    #print(edges[18][0], edges[18][1])
    #print(edges[19][0], edges[19][1])
    #print(edges[20][0], edges[20][1])
    #print(edges[21][0], edges[21][1])
    #print(edges[22][0], edges[22][1])
    #print(edges[23][0], edges[23][1])
    #print(edges[24][0], edges[24][1])
    #print(edges[25][0], edges[25][1])
    #print(edges[26][0], edges[26][1])
    #print(edges[27][0], edges[27][1])
    #print(edges[28][0], edges[28][1])
    #

=======
Suggestion 9

def dfs(now, color):
    global res
    visited[now] = color
    if color == 1:
        res += 1
    for nxt in G[now]:
        if visited[nxt] == -1:
            dfs(nxt, 1 - color)
        elif visited[nxt] == color:
            print(0)
            exit()
    return

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

visited = [-1] * N
res = 0
dfs(0, 0)
print(res * (N - res) - M)

=======
Suggestion 10

def solve():
    pass
