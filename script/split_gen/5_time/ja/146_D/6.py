def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * (N-1)
    c = 0
    for i in range(N):
        if len(G[i]) > c:
            c = len(G[i])
            s = i
    color = [0] * N
    color[s] = 1
    q = [s]
    while q:
        v = q.pop()
        c = 1
        for i in range(len(G[v])):
            u = G[v][i]
            if color[u] == 0:
                if c == color[v]:
                    c += 1
                color[u] = c
                ans[i] = c
                c += 1
                q.append(u)
    print(max(color))
    for i in range(N-1):
        print(ans[i])
