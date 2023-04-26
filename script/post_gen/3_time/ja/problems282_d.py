Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())

    print(N, M)
    print(u)
    print(v)

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [0] * n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            b = color.count(1)
            ans += b * (b - 1) // 2
            c = color.count(-1)
            ans += c * (c - 1) // 2
        else:
            print(0)
            exit()
print(ans)

=======
Suggestion 3

def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

color = [0] * N
ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            cnt1 = color.count(1)
            cnt2 = color.count(-1)
            ans += cnt1 * cnt2
        else:
            ans = -1
            break
print(ans)

=======
Suggestion 4

def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
color = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            cnt1 = color.count(1)
            cnt2 = color.count(-1)
            ans += cnt1 * cnt2
        else:
            ans += N * (N - 1) // 2
            break
print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    from collections import deque
    q = deque([0])
    color = [-1] * n
    color[0] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)

    cnt = [0] * 2
    for c in color:
        cnt[c] += 1
    print(cnt[0] * cnt[1] - m)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)

    print(u)
    print(v)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    #print(N, M)
    #print(u, v)
    #グラフGを作る
    G = [[] for i in range(N)]
    for i in range(M):
        G[u[i]-1].append(v[i]-1)
        G[v[i]-1].append(u[i]-1)
    #print(G)
    #print(len(G[0]))
    #print(len(G[4]))
    #print(len(G[2]))
    #print(len(G[1]))
    #print(len(G[3]))
    #print(len(G[5]))
    #print(len(G[6]))
    #print(len(G[7]))
    #print(len(G[8]))
    #print(len(G[9]))
    #print(len(G[10]))
    #print(len(G[11]))
    #print(len(G[12]))
    #print(len(G[13]))
    #print(len(G[14]))
    #print(len(G[15]))
    #print(len(G[16]))
    #print(len(G[17]))
    #print(len(G[18]))
    #print(len(G[19]))
    #print(len(G[20]))
    #print(len(G[21]))
    #print(len(G[22]))
    #print(len(G[23]))
    #print(len(G[24]))
    #print(len(G[25]))
    #print(len(G[26]))
    #print(len(G[27]))
    #print(len(G[28]))
    #print(len(G[29]))
    #print(len(G[30]))
    #print(len(G[31]))
    #print(len(G[32]))
    #print(len(G[33]))
    #print(len(G[34]))
    #print(len(G[35]))
    #print(len(G[36]))
    #print(len(G[37]))
    #print(len(G[38]))
    #print(len(G[39]))
    #print(len(G[40]))
    #print(len(G[41]))
    #print(len(G[42]))
    #print(len(G[43]))
    #print(len(G[44]))
    #print(len(G[45]))
    #print(len(G

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(m)]
    adj = [[] for _ in range(n+1)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    ans = 0
    for u,v in edge:
        color = [0]*(n+1)
        color[u] = 1
        color[v] = 2
        q = [u,v]
        while q:
            p = q.pop()
            for i in adj[p]:
                if color[i] == 0:
                    color[i] = 3 - color[p]
                    q.append(i)
                elif color[i] == color[p]:
                    ans += 1
                    break
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    # 連結なグラフを作成する
    # 連結でないグラフの場合、二部グラフにならないから
    # 連結なグラフの場合、二部グラフになるとは限らないが、
    # 二部グラフにならない場合は、条件を満たさないので、条件を満たす組は0になる
    # 連結なグラフを作成する
    # 連結でないグラフの場合、二部グラフにならないから
    # 連結なグラフの場合、二部グラフになるとは限らないが、
    # 二部グラフにならない場合は、条件を満たさないので、条件を満たす組は0になる
    # 連結なグラフを作成する
    # 連結でないグラフの場合、二部グラフにならないから
    # 連結なグラフの場合、二部グラフになるとは限らないが、
    # 二部グラフにならない場合は、条件を満たさないので、条件を満たす組は0になる
    # 連結なグラフを作成する
    # 連結でないグラフの場合、二部グラフにならないから
    # 連結なグラフの場合、二部グラフになるとは限らないが、
    # 二部グラフにならない場合は、条件を満たさないので、条件を満たす組は0になる
    # 連

=======
Suggestion 10

def solve():
    pass
