Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    #print(n,m)
    #print(type(n),type(m))
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    #print(edges)
    #print(type(edges))
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    #print(graph)
    #print(type(graph))
    ans = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if j not in graph[i]:
                #print(i,j)
                #print(graph[i])
                #print(graph[j])
                ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    d = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    print(sum(i == 1 for i in d))

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    # 1. 读取边
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    # 2. 构建邻接表
    adj = [[] for _ in range(N+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # 3. 构建双线图
    # 黑色：0，白色：1，未涂色：-1
    colors = [-1] * (N+1)
    def dfs(u, color):
        colors[u] = color
        for v in adj[u]:
            if colors[v] == -1:
                dfs(v, 1-color)
    dfs(1, 0)
    # 4. 统计答案
    ans = 0
    for u, v in edges:
        if colors[u] != colors[v]:
            ans += 1
    print(ans)

solve()

=======
Suggestion 5

def solve():
    N,M = map(int,input().split())
    u = [0]*M
    v = [0]*M
    for i in range(M):
        u[i],v[i] = map(int,input().split())
    #print(N,M,u,v)
    #print(len(u),len(v))
    #print(u[0],v[0])
    #print(u[1],v[1])
    #print(u[2],v[2])
    #print(u[3],v[3])
    #print(u[4],v[4])
    #print(u[5],v[5])
    #print(u[6],v[6])
    #print(u[7],v[7])
    #print(u[8],v[8])
    #print(u[9],v[9])
    #print(u[10],v[10])
    #print(u[11],v[11])
    #print(u[12],v[12])
    #print(u[13],v[13])
    #print(u[14],v[14])
    #print(u[15],v[15])
    #print(u[16],v[16])
    #print(u[17],v[17])
    #print(u[18],v[18])
    #print(u[19],v[19])
    #print(u[20],v[20])
    #print(u[21],v[21])
    #print(u[22],v[22])
    #print(u[23],v[23])
    #print(u[24],v[24])
    #print(u[25],v[25])
    #print(u[26],v[26])
    #print(u[27],v[27])
    #print(u[28],v[28])
    #print(u[29],v[29])
    #print(u[30],v[30])
    #print(u[31],v[31])
    #print(u[32],v[32])
    #print(u[33],v[33])
    #print(u[34],v[34])
    #print(u[35],v[35])
    #print(u[36],v[36])
    #print(u[37],v[37])
    #print(u[38],v[38])
    #print(u[

=======
Suggestion 6

def solve(n, m, u, v):
    # 从1开始，所以需要n+1
    color = [0] * (n + 1)
    # 从1开始，所以需要n+1
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    # print(g)
    ans = 0
    for i in range(1, n + 1):
        # 如果当前节点没有被染色
        if color[i] == 0:
            # 从当前节点开始染色
            ans += 1
            q = [i]
            color[i] = 1
            while len(q) != 0:
                cur = q.pop()
                # 遍历当前节点的所有邻接边
                for j in g[cur]:
                    # 如果当前节点和邻接边的颜色相同，返回False
                    if color[j] == color[cur]:
                        return 0
                    # 如果邻接边没有被染色，那么染成和当前节点不同的颜色
                    if color[j] == 0:
                        color[j] = -color[cur]
                        q.append(j)
    return ans

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    ans = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if j in graph[i]:
                continue
            for k in graph[i]:
                if k in graph[j]:
                    break
            else:
                ans += 1
    print(ans)

=======
Suggestion 8

def get_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    return n, m, edges

=======
Suggestion 9

def main():
    return
