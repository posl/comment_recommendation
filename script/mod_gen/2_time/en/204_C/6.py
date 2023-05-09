def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        q = [i]
        while q:
            v = q.pop()
            for nv in G[v]:
                if not visited[nv]:
                    visited[nv] = True
                    q.append(nv)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    main()