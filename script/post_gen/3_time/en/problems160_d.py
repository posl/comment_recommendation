Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            dist[d] += 1

    for i in range(1, N):
        print(dist[i])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist[min(j - i, abs(i - X) + 1 + abs(j - Y))] += 1
    for i in range(1, N):
        print(dist[i])

=======
Suggestion 3

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if i < X < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            else:
                d = j - i
            dist[d] += 1
    for k in range(1, N):
        print(dist[k])

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * (N-1)
    for i in range(N):
        for j in range(i+1, N):
            d = min(j-i, abs(X-i)+abs(Y-j)+1)
            dist[d-1] += 1
    for d in dist:
        print(d)

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * N

    for i in range(N):
        for j in range(i+1, N):
            d = min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
            dist[d] += 1

    for i in range(1, N):
        print(dist[i])

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N-1)
    for i in range(N):
        for j in range(i+1, N):
            dist = min(j-i, abs(X-i)+1+abs(Y-j))
            ans[dist-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 8

def solve():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            dist[d - 1] += 1
    for x in dist:
        print(x)

solve()

=======
Suggestion 9

def getG(N):
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    return G

=======
Suggestion 10

def shortest_paths(graph, start):
    """Find shortest paths from start vertex to all other vertices of a graph
    graph is represented as a dictionary mapping vertices to iterables of
    neighbouring vertices.  start is the vertex from which to start
    shortest path search, and it is assumed to be a vertex of graph"""
    Q = set(graph) # set of all unvisited nodes
    dist = {} # dictionary of final distances
    for v in Q:
        dist[v] = float("inf") # unknown distance function from source to v
    dist[start] = 0 # distance from source to source
    while Q: # while Q is non-empty
        u = min(Q, key=dist.get) # vertex in Q with smallest distance
        Q.remove(u)
        for v in graph[u]: # where v has not yet been removed from Q.
            alt = dist[u] + 1 # length of this path
            if alt < dist[v]: # if new path is shorter
                dist[v] = alt # update distance
    return dist
