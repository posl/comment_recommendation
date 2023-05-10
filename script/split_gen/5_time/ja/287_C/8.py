def main():
    n, m = map(int, input().split())
    if m == 0:
        print("No")
        exit()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n + 1):
        if len(graph[i]) == 2:
            print("Yes")
            exit()
    print("No")
