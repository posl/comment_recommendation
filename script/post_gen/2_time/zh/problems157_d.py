Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

=======
Suggestion 2

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def DFS(G, v):
    visited[v] = True
    for i in range(len(G[v])):
        if not visited[G[v][i]]:
            DFS(G, G[v][i])

N, M, K = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

G = [[] for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

visited = [False for i in range(N + 1)]
for i in range(K):
    visited[C[i]] = True
    visited[D[i]] = True
for i in range(1, N + 1):
    if not visited[i]:
        DFS(G, i)
        break

ans = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    ans[i] = len(G[i]) - 1 - sum(visited[j] for j in G[i])

print(*ans[1:])

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def getFriends(N,M,K,AB,CD):
    #先建立邻接表
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[AB[i][0]-1].append(AB[i][1]-1)
        adj[AB[i][1]-1].append(AB[i][0]-1)
    #print(adj)
    #再建立阻隔表
    block = [[] for _ in range(N)]
    for i in range(K):
        block[CD[i][0]-1].append(CD[i][1]-1)
        block[CD[i][1]-1].append(CD[i][0]-1)
    #print(block)
    #最后判断是否是候选好友
    res = []
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i!=j and j not in adj[i] and j not in block[i]:
                tmp += 1
        res.append(tmp)
    return res

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    friends = [[] for _ in range(n)]
    blocks = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    for i in range(n):
        ans = 0
        for j in range(n):
            if i == j:
                continue
            if j in friends[i]:
                continue
            if j in blocks[i]:
                continue
            if reachable(friends, i, j, n):
                ans += 1
        print(ans, end=" ")
    print()

=======
Suggestion 7

def main():
    # 读取输入
    N, M, K = map(int, input().split())
    # 读取友谊关系
    friends = [tuple(map(int, input().split())) for i in range(M)]
    # 读取阻隔关系
    blocks = [tuple(map(int, input().split())) for i in range(K)]
    # 生成邻接表
    adj = [[] for i in range(N)]
    for f in friends:
        adj[f[0]-1].append(f[1]-1)
        adj[f[1]-1].append(f[0]-1)
    # 生成距离表
    dist = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i] = 0
        queue = [i]
        while len(queue) > 0:
            v = queue.pop(0)
            for u in adj[v]:
                if dist[i][u] < 0:
                    dist[i][u] = dist[i][v] + 1
                    queue.append(u)
    # 计算结果
    result = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if dist[i][j] < 0:
                continue
            if dist[i][j] == 1:
                continue
            for b in blocks:
                if b[0] == i+1 and b[1] == j+1:
                    break
                if b[0] == j+1 and b[1] == i+1:
                    break
            else:
                result[i] += 1
    # 输出结果
    print(" ".join(map(str, result)))

=======
Suggestion 8

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for _ in range(k):
    c, d = map(int, input().split())
    graph[c-1].append(d-1)
    graph[d-1].append(c-1)

visited = [False for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
    ans[i] = visited.count(False) - 1
    visited = [False for _ in range(n)]

print(*ans)

=======
Suggestion 9

def main():
    #读取输入
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #建立友谊关系图
    friends = [[] for _ in range(N)]
    for a, b in AB:
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #建立阻隔关系图
    blocks = [[] for _ in range(N)]
    for c, d in CD:
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #候选好友列表
    candidates = [0]*N
    #遍历所有用户
    for i in range(N):
        #遍历所有用户的好友
        for j in friends[i]:
            #如果用户i和用户j之间不存在友谊关系
            if i not in friends[j]:
                #如果用户i和用户j之间不存在阻隔关系
                if i not in blocks[j]:
                    #如果用户i和用户j之间存在路径
                    if path(friends, i, j):
                        #用户j是用户i的候选好友
                        candidates[i] += 1
    #打印答案
    print(*candidates)
