Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    # print(a, b)
    # 从西边来的第i个岛和从西边来的第（i+1）个岛之间发生了争端。
    # 请使这些

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N - 1 - len(set(A)) - len(set(B)))

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    a_b = []
    for i in range(M):
        a_b.append([a[i], b[i]])
    a_b.sort()
    a = []
    b = []
    for i in range(M):
        a.append(a_b[i][0])
        b.append(a_b[i][1])
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    ans = 0
    for i in range(len(a)):
        ans += (b[i] - a[i] - 1)
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    bridge = []
    for _ in range(m):
        a, b = map(int, input().split())
        bridge.append((a, b))

    bridge.sort()

    # print(bridge)

    bridge_set = set()
    for i in range(m):
        bridge_set.add(bridge[i])

    # print(bridge_set)

    # print(bridge_set)

    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for v in graph[vertex]:
                    stack.append(v)
        return visited

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for i in range(m):
        graph[bridge[i][0]].append(bridge[i][1])
        graph[bridge[i][1]].append(bridge[i][0])

    # print(graph)

    # print(dfs(graph, 1))

    count = 0
    for i in range(1, n + 1):
        if i not in dfs(graph, 1):
            count += 1

    print(count - 1)

    # print(graph)

    # print(dfs(graph, 1))

=======
Suggestion 6

def main():
    print('Hello World!')

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(solve(N,M,A,B))

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    #print(n,m)
    #print(type(n),type(m))
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)

    #各个岛屿的连接数
    c = [0 for i in range(n)]
    for i in range(m):
        c[a[i]-1] += 1
        c[b[i]-1] += 1
    #print(c)

    #计算桥梁数
    bridge = 0
    for i in range(n):
        bridge += c[i]//2
    #print(bridge)

    #计算拆除桥梁数
    #拆除桥梁的条件：必须是两个岛屿之间的桥梁，且岛屿的连接数都大于2
    remove = 0
    for i in range(m):
        if c[a[i]-1] > 2 and c[b[i]-1] > 2:
            remove += 1
    #print(remove)

    #print(bridge - remove)
    print(bridge - remove)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab,key=lambda x:x[1])
    #print(ab)
    count = 0
    for i in range(m):
        if ab[i][0] == 1:
            count +=1
    print(count)

=======
Suggestion 10

def dfs(v):
    global k
    if visited[v]:
        return
    visited[v] = True
    for i in range(1, n+1):
        if G[v][i] == 1:
            dfs(i)
        elif G[v][i] == 2:
            k += 1
            G[v][i] = 0
            G[i][v] = 0
            dfs(i)

n, m = map(int, input().split())
G = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
visited = [False] * (n+1)
k = 0
dfs(1)
print(k)
