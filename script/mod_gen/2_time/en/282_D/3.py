def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * (N - 1) // 2)
        return
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        Q = [i]
        c = 0
        d = 0
        while Q:
            q = Q.pop()
            c += 1
            for j in G[q]:
                if visited[j]:
                    continue
                visited[j] = True
                Q.append(j)
                d += 1
        ans += c * d
    print(ans)

if __name__ == '__main__':
    main()