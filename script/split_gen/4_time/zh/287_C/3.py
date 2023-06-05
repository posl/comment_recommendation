def main():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(N):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return
