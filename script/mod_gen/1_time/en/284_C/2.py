def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            queue = [i]
            while queue:
                now = queue.pop()
                for next in graph[now]:
                    if visited[next] == False:
                        visited[next] = True
                        queue.append(next)
    print(ans)

if __name__ == '__main__':
    main()