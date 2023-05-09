def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        G[u].append(v)
        G[v].append(u)
    from collections import deque
    def bfs(s):
        q = deque([s])
        color = [-1]*N
        color[s] = 0
        while q:
            u = q.popleft()
            for v in G[u]:
                if color[v] == -1:
                    color[v] = color[u]^1
                    q.append(v)
        return color
    color = bfs(0)
    cnt = [0]*2
    for c in color:
        cnt[c] += 1
    ans = cnt[0]*cnt[1] - M
    print(ans)
