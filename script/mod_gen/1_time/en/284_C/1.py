def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    used = [False] * N
    ans = 0
    for i in range(N):
        if used[i]:
            continue
        ans += 1
        q = [i]
        while q:
            v = q.pop()
            used[v] = True
            for nv in G[v]:
                if used[nv]:
                    continue
                q.append(nv)
    print(ans)

if __name__ == '__main__':
    main()