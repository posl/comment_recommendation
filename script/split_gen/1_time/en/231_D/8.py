def main():
    # Read data
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # Initialize graph
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # Initialize visited
    visited = [-1] * N
    # Search
    def dfs(v, color):
        visited[v] = color
        for nv in graph[v]:
            if visited[nv] == color:
                return False
            if visited[nv] == -1 and not dfs(nv, 1 - color):
                return False
        return True
    # Output
    for i in range(N):
        if visited[i] == -1 and not dfs(i, 0):
            print("No")
            return
    print("Yes")
