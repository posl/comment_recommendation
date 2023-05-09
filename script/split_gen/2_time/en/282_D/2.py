def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    color = [-1] * n
    ans = 0
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q = [i]
        while q:
            v = q.pop()
            for nv in graph[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v]
                    q.append(nv)
                elif color[nv] == color[v]:
                    print(0)
                    return
        cnt = [0, 0]
        for c in color:
            cnt[c] += 1
        ans += cnt[0] * cnt[1] - m
    print(ans)
