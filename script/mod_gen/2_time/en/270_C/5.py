def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        d = [0] * N
        q = [i]
        while q:
            v = q.pop()
            for nv in G[v]:
                if d[nv] == 0:
                    d[nv] = d[v] + 1
                    q.append(nv)
        if d[Y] != 0:
            ans[d[Y]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            break
        print(ans[i])

if __name__ == '__main__':
    main()