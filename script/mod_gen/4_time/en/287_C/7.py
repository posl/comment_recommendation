def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n+1)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,n+1):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()