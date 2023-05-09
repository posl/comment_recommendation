def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    graph = [[] for _ in range(N+1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (N+1)
    visited[1] = True
    ans = [1]
    stack = [1]
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            ans.append(v)
            stack.append(v)
            break
        else:
            ans.append(1)
    print(*ans)

if __name__ == '__main__':
    main()