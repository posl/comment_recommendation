def main():
    N, X, Y = map(int, input().split())
    X, Y = X - 1, Y - 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)
    
    ans = [0] * N
    for i in range(N):
        if i != X:
            q = [i]
            visited = [False] * N
            visited[i] = True
            while q:
                v = q.pop()
                if v == X:
                    ans[i] = len(q) + 1
                    break
                for nv in graph[v]:
                    if not visited[nv]:
                        visited[nv] = True
                        q.append(nv)
    for i in range(N):
        if i != Y:
            q = [i]
            visited = [False] * N
            visited[i] = True
            while q:
                v = q.pop()
                if v == Y:
                    ans[i] = len(q) + 1
                    break
                for nv in graph[v]:
                    if not visited[nv]:
                        visited[nv] = True
                        q.append(nv)
    for i in range(N):
        if i != X and i != Y:
            print(ans[i])

if __name__ == '__main__':
    main()