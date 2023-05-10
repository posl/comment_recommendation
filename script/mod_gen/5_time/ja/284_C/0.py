def main():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            stack = [i]
            while len(stack) > 0:
                v = stack.pop()
                for nv in graph[v]:
                    if visited[nv] == False:
                        visited[nv] = True
                        stack.append(nv)
    print(ans)

if __name__ == '__main__':
    main()