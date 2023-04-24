Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append([v - 1, w])
        G[v - 1].append([u - 1, w])

    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        now = que.pop()
        for nxt, w in G[now]:
            if ans[nxt] != -1:
                continue
            ans[nxt] = ans[now] if w % 2 == 0 else 1 - ans[now]
            que.append(nxt)
    print(*ans, sep='

')

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    # 深さ優先探索
    # 訪問済みにする
    # 隣接リストを辿っていく
    # 隣接リストが偶数か奇数かで色を変える

    # 隣接リストが偶数か奇数かで色を変える
    # 1: 白
    # 0: 黒
    color = [None] * N
    color[0] = 1

    # 訪問済みにする
    visited = [False] * N
    visited[0] = True

    # 深さ優先探索
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            if w % 2 == 0:
                color[nv] = color[v]
            else:
                color[nv] = 1 - color[v]
            stack.append(nv)

    for c in color:
        print(c)

main()

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        ans[v] = ans[p] + G[v][p][1]
        for i, (nv, w) in enumerate(G[v]):
            if nv == p:
                continue
            stack.append((nv, v))

    for i in range(N):
        print(ans[i] % 2)

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))

    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        v, d = stack.pop()
        ans[v] = d % 2
        for u, w in G[v]:
            if ans[u] == -1:
                stack.append((u, d + w))

    print(*ans, sep='

')

=======
Suggestion 5

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    dp = [-1] * N
    dp[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in G[i]:
            if dp[j] == -1:
                dp[j] = dp[i] ^ (w % 2)
                stack.append(j)
    print(*dp, sep='

')

=======
Suggestion 6

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    #print(G)

    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        v, c = stack.pop()
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (c + w) % 2
                stack.append((nv, color[nv]))

    for c in color:
        print(c)

=======
Suggestion 7

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))

    color = [-1] * n
    color[0] = 0
    que = [(0, 0)]
    while que:
        now, c = que.pop()
        for nxt, w in tree[now]:
            if color[nxt] == -1:
                color[nxt] = c ^ (w % 2)
                que.append((nxt, color[nxt]))

    print(*color, sep='

')

=======
Suggestion 8

def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))

    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for to, w in edge[now]:
            if color[to] != -1:
                continue
            if w % 2 == 0:
                color[to] = color[now]
            else:
                color[to] = 1 - color[now]
            stack.append(to)

    for c in color:
        print(c)

=======
Suggestion 9

def main():
    N = int(input())
    V = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        V[u - 1].append((v - 1, w))
        V[v - 1].append((u - 1, w))
    #print(V)
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in V[v]:
            if color[u] == -1:
                color[u] = (color[v] + w) % 2
                stack.append(u)
    for c in color:
        print(c)

=======
Suggestion 10

def main():
    import sys
    #N
    N = int(input())
    #u_1 v_1 w_1
    #u_2 v_2 w_2
    #.
    #.
    #.
    #u_{N - 1} v_{N - 1} w_{N - 1}
