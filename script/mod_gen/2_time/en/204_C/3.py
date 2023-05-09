def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False]*N
        q = [i]
        while q:
            v = q.pop()
            if not visited[v]:
                visited[v] = True
                for j in G[v]:
                    q.append(j)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    main()