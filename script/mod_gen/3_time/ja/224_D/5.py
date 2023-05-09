def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    G = [[] for _ in range(9)]
    for _ in range(N):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    S = list(map(int, input().split()))
    for i in range(8):
        S[i] -= 1
    S[8] = -1
    def bfs(s, t):
        q = [s]
        d = [-1] * 9
        d[s] = 0
        while len(q) > 0:
            v = q.pop(0)
            for u in G[v]:
                if d[u] != -1:
                    continue
                d[u] = d[v] + 1
                q.append(u)
        return d[t]
    ans = 10**9
    for i in range(8):
        for j in range(i+1, 8):
            ans = min(ans, bfs(S[i], S[j])+1)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()