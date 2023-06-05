Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        temp = input().split()
        edges.append([int(temp[0]),int(temp[1]),int(temp[2])])
    edges.sort(key=lambda x:x[2])
    edges.reverse()
    sum = 0
    for i in range(n-1):
        sum += edges[i][2]*(i+1)*(n-i-1)
    print(sum)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # print(G)

    # BFS
    from collections import deque
    def bfs(s):
        dist = [-1] * N
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u, w in G[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + w
                    q.append(u)
        return dist

    dist = bfs(0)
    # print(dist)
    max_dist = max(dist)
    max_idx = dist.index(max_dist)
    dist = bfs(max_idx)
    # print(dist)
    print(sum(dist))

main()

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    N = int(input())
    uvw = [list(map(int, input().split())) for _ in range(N-1)]
    # print(N)
    # print(uvw)
    # N = 3
    # uvw = [[1,2,10],[2,3,20]]
    # N = 5
    # uvw = [[1,2,1],[2,3,2],[4,2,5],[3,5,14]]
    # N = 8
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3],[8,5,9],[7,5,8]]
    # N = 6
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3]]
    # N = 6
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3],[6,5,4]]
    # N = 6
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3],[6,5,4],[6,4,6]]
    # N = 6
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3],[6,5,4],[6,4,6],[6,3,7]]
    # N = 6
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14],[1,5,3],[6,5,4],[6,4,6],[6,3,7],[6,1,8]]
    #

=======
Suggestion 6

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += edges[i][2] * edges[j][2]
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    sizes = [1 for i in range(n)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if sizes[x] < sizes[y]:
            x, y = y, x
        parents[y] = x
        sizes[x] += sizes[y]
        return True
    ans = 0
    for u, v, w in edges:
        u, v = u - 1, v - 1
        ans += w * sizes[find(u)] * sizes[find(v)]
        union(u, v)
    print(ans)
