Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())

    # 从1号房间开始，通过通道移动到达的房间
    to = [[] for _ in range(n + 1)]
    for i in range(m):
        to[a[i]].append(b[i])
        to[b[i]].append(a[i])

    # 求解
    ans = [0] * (n + 1)
    ans[1] = 1
    for i in to[1]:
        ans[i] = 1
    for i in to[1]:
        for j in to[i]:
            if ans[j] == 0:
                ans[j] = i

    # 输出结果
    print("Yes")
    for i in range(2, n + 1):
        print(ans[i])

=======
Suggestion 3

def dfs(v):
    global ans
    global flag
    if flag == False:
        return
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            ans[i-1] = v
            dfs(i)
        else:
            if ans[v-1] != i:
                flag = False
                return

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
flag = True
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)

=======
Suggestion 4

def dfs(v):
    global flag
    for i in range(len(g[v])):
        if visited[g[v][i]] == 0:
            visited[g[v][i]] = 1
            if g[v][i] == 1:
                flag = True
                return
            dfs(g[v][i])
            if flag:
                return
        else:
            continue

n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
flag = False
visited[1] = 1
dfs(1)

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for next_v in graph[v]:
        dfs(next_v)
    ans.append(v+1)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
visited = [False] * N
ans = []
for i in range(N):
    dfs(i)
print('Yes')
for i in range(N-1):
    print(ans[i+1])
