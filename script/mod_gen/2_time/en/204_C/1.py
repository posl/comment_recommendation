def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for nv in G[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                stack.append(nv)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    main()