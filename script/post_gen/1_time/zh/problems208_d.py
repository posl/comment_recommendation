Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(n, m)
    #print(type(n), type(m))
    print(type(n), ty

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A, B, C = [], [], []
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # Floyd–Warshall algorithm
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    # https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
    # https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
    # https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph/
    # https://www.geeksforgeeks.org/shortest-path-with-exactly-k-edges-in-a-directed-and-weighted-graph-set-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-3/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-4/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-5-dijkstra-clone/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-6-dag/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-7-dynamic-programming/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-8-dynamic-programming-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-9-oeksp-using-matrix-power/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-10-dp-optimization/
    # https://www.geeksforgeeks.org/shortest-path-exactly

=======
Suggestion 4

def floyd_warshall(d):
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

N, M = map(int, input().split())
d = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
floyd_warshall(d)
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            ans += d[i][j] if d[i][j] < float('inf') and d[i][j] == d[i][k]+d[k][j] else 0
print(ans)

=======
Suggestion 5

def main():
    #读入数据
    n,m = map(int,input().split())
    a,b,c = [0]*m,[0]*m,[0]*m
    for i in range(m):
        a[i],b[i],c[i] = map(int,input().split())
    #初始化
    d = [[float('inf')]*n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[a[i]-1][b[i]-1] = c[i]
    #Floyd-Warshall算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    #计算结果
    result = 0
    for s in range(n):
        for t in range(n):
            for k in range(n):
                if d[s][t] == d[s][k]+d[k][t]:
                    result += d[s][t]
    print(result)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][i] = 0
    for i in range(m):
        s,t,k = map(int, input().split())
        a[s-1][t-1] = k
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = min(a[i][j], a[i][k]+a[k][j])
    
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][j] == a[i][k] + a[k][j]:
                    ans += a[i][j]
    print(ans)

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    graph = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(m):
        a,b,c = map(int, input().split())
        graph[a-1][b-1] = c
    for i in range(n):
        graph[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    res += graph[i][j]
    print(res)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    d = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        a,b,c = map(int,input().split())
        d[a-1][b-1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue
                ans += d[i][j]+d[j][k]
    print(ans)
