def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False] * N
        q = [i]
        visited[i] = True
        while q:
            v = q.pop()
            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    main()