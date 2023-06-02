Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(M)]
    uv.sort()
    for i in range(M):
        uv[i].sort()
    uv.sort(key=lambda x: x[0])
    print(uv)
    for i in range(N):
        if uv[i][0] != i+1:
            print('No')
            exit()
    else:
        print('Yes')

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    u = [0] * m
    v = [0] * m
    for i in range(m):
        u[i],v[i] = map(int,input().split())
    ans = 'Yes'
    for i in range(m):
        if u[i] > v[i]:
            u[i],v[i] = v[i],u[i]
    for i in range(1,n+1):
        if u.count(i) > 1:
            ans = 'No'
            break
    if ans == 'Yes':
        for i in range(m-1):
            if v[i] != u[i+1]:
                ans = 'No'
                break
    print(ans)

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(N):
        if len(graph[i])>2:
            print('No')
            return
    print('Yes')
solve()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    for i in range(n):
        if len(edge[i]) > 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(n):
        graph[i].sort()
    for i in range(n):
        if graph[i] != list(range(min(i+2,n),max(i-1,0),-1)):
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def isPathGraph(n, m, u, v):
    if m != n-1:
        return False
    for i in range(m):
        if abs(u[i]-v[i]) != 1:
            return False
    return True

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    # 读入数据
    N, M = map(int, input().split())
    # 建立邻接表
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    # DFS判断是否为路径图
    seen = [False] * N
    def dfs(v):
        seen[v] = True
        if len(adj[v]) == 1:
            return True
        for nv in adj[v]:
            if seen[nv]:
                continue
            if not dfs(nv):
                return False
        return True
    for v in range(N):
        if seen[v]:
            continue
        if not dfs(v):
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    if m != n-1:
        print("No")
        return
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n):
        graph[i].sort()
    for i in range(n):
        if graph[i] != [i-1,i+1]:
            print("No")
            return
    print("Yes")
