Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m=map(int,input().split())
    a=[0]*m
    b=[0]*m
    for i in range(m):
        a[i],b[i]=map(int,input().split())
    print(m)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 从西边连接第i个岛和从西边连接第（i+1）个岛
    # 从西边连接第a_i个岛和从西边连接第b_i个岛
    # 1 2 3 4 5
    # 1 4
    # 2 5
    # 1和4之间有桥梁，2和5之间有桥梁
    # 1和4之间有桥梁，1和5之间有桥梁
    # 1和4之间有桥梁，2和4之间有桥梁
    # 1和4之间有桥梁，2和5之间有桥梁
    # 1和4之间有桥梁，3和4之间有桥梁
    # 1和4之间有桥梁，3和5之间有桥梁
    # 1和4之间有桥梁，4和5之间有桥梁
    # 2和5之间有桥梁，1和5之间有桥梁
    # 2和5之间有桥梁，2和4之间有桥梁
    # 2和5之间有桥梁，2和5之间有桥梁
    # 2和5之间有桥梁，3和4之间有桥梁
    # 2和5之间有桥梁，3和5之间有桥梁
    # 2和5之间有桥梁，4和5之间有桥梁
    # 1和2之间有桥梁

=======
Suggestion 3

def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]

=======
Suggestion 4

def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    ans = 0
    for i in range(m):
        if a[i] != 1 and b[i] != 1:
            ans += 1
    print(ans)

=======
Suggestion 6

def dfs(x, y):
    global n, m, a, b, visited, graph
    visited[x] = True
    for i in range(len(graph[x])):
        if graph[x][i] == y:
            graph[x][i] = 0
            graph[y][i] = 0
            return
    for i in range(len(graph[x])):
        if graph[x][i] != 0 and visited[graph[x][i]] == False:
            dfs(graph[x][i], y)


n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
graph = [[] for _ in range(n+1)]
for i in range(m):
    graph[a[i]].append(b[i])
    graph[b[i]].append(a[i])
ans = 0
for i in range(m):
    visited = [False for _ in range(n+1)]
    dfs(a[i], b[i])
    if visited.count(True) != n:
        ans += 1
print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(1))

=======
Suggestion 8

def get_input():
    N, M = map(int, input().split())
    for i in range(M):
        a, b = map(int, input().split())
        yield a, b

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(A)
    # print(B)
    # print(N)
    # print(M)

    # 与えられたM個の橋のうち、何個の橋を壊せばよいかを求める。
    # つまり、M個の橋のうち、何個の橋を壊せないかを求める。
    # つまり、M個の橋のうち、何個の橋が必要かを求める。
    # つまり、M個の橋のうち、何個の橋が重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の橋のうち、何個の橋が両方向に重複しているかを求める。
    # つまり、M個の

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(M)]
    a_b.sort(key=lambda x: x[1])
    count = 0
    bridge = [False] * N
    for i in range(M):
        if bridge[a_b[i][0]-1] == False and bridge[a_b[i][1]-1] == False:
            bridge[a_b[i][1]-1] = True
            count += 1
    print(count)
