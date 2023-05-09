def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = list(map(lambda x: x - 1, A))
    B = list(map(lambda x: x - 1, B))
    graph = [[] for _ in range(N)]
    for i in range(M):
        graph[A[i]].append(B[i])
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for j in graph[v]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    main()