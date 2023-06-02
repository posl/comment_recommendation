Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    #pr

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    u = []
    v = []
    for i in range(m):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    print(n)
    print(m)
    print(u)
    print(v)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, edges)

    # 邻接表
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    # print(adj)

    # 1. 无向图G没有一条连接顶点u和顶点v的边
    # 2. 在图G中增加一条连接顶点u和顶点v的边，就形成了一个双线图
    # 3. 双线图是二分图
    # 4. 二分图中没有奇数环
    # 5. 二分图中最大独立集等于顶点数减去最大匹配数

    # 二分图检测
    # 1. 深度优先遍历
    # 2. 广度优先遍历
    # 3. 染色法
    # 4. 邻接矩阵
    # 5. 邻接表

    # 染色法
    # 1. 从任意一个顶点开始，将其染成红色
    # 2. 将与其相邻的顶点染成蓝色
    # 3. 将与蓝色顶点相邻的顶点染成红色
    # 4. 如果某个顶点的相邻顶点已经染成了同色，则不是二分图
    # 5. 如果所有顶点都染完了，则是二分图
    # 6. 时间复杂度O(V+E)
    # 7. 空间复杂度O(V)

    # 二分图中最大独立集等于顶点数减去最大匹配数
    #

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    uv = []
    for i in range(M):
        uv.append(list(map(int, input().split())))
    ans = 0
    for i in range(M):
        u = uv[i][0]
        v = uv[i][1]
        for j in range(M):
            if i == j:
                continue
            if uv[j][0] == u and uv[j][1] == v:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    N, M = map(int, input().split())
    if 2 <= N <= 2 * 10 ** 5 and 0 <= M <= min(2 * 10 ** 5, N * (N - 1) / 2):
        print('N = {}, M = {}'.format(N, M))
    else:
        print('N or M is not in the range')
        exit()
    return N, M

=======
Suggestion 6

def dfs(i, color):
    global flag
    global colors
    global visited
    # 如果已经找到了不合法的情况，就不用再找了
    if flag == 0:
        return
    # 如果已经访问过，就不用再访问了
    if visited[i] == 1:
        return
    # 如果当前点已经染色了，就看看和之前的颜色是否相同
    if colors[i] != 0:
        if colors[i] == color:
            # 如果颜色相同，就找到了不合法的情况
            flag = 0
        return
    # 如果当前点没有染色，就染上颜色
    colors[i] = color
    # 并且标记为已经访问
    visited[i] = 1
    # 然后遍历所有与当前点相邻的点
    for j in range(len(graph[i])):
        # 如果当前点和相邻的点颜色相同，就找到了不合法的情况
        if colors[graph[i][j]] == color:
            flag = 0
            return
        # 如果当前点和相邻的点颜色不同，就继续遍历相邻的点
        else:
            dfs(graph[i][j], -color)

=======
Suggestion 7

def dfs(i, color):
    global G, visited, colors
    visited[i] = True
    colors[i] = color
    for j in G[i]:
        if visited[j]:
            if colors[j] == color:
                return False
        else:
            if not dfs(j, 1 - color):
                return False
    return True

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

visited = [False] * n
colors = [-1] * n
ans = 0
for i in range(n):
    if not visited[i]:
        if dfs(i, 0):
            b = colors.count(0)
            w = colors.count(1)
            ans += b * (b - 1) // 2 + w * (w - 1) // 2
        else:
            ans = -1
            break
print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if color[nv] == -1:
                color[nv] = 1 - color[v]
                stack.append(nv)

    color_num = [0, 0]
    for c in color:
        color_num[c] += 1

    ans = color_num[0] * color_num[1] - m
    print(ans)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    u = [0] * m
    v = [0] * m
    for i in range(m):
        u[i], v[i] = map(int, input().split())
    print(n * (n - 1) // 2 - m)
    return 0

=======
Suggestion 10

def main():
    pass
