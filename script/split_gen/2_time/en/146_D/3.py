def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        G[a].append((b, i))
        G[b].append((a, i))
    color = [-1] * (N-1)
    def dfs(v, p, c):
        k = 1
        for w, i in G[v]:
            if w == p: continue
            if k == c: k += 1
            color[i] = k
            dfs(w, v, k)
            k += 1
    dfs(0, -1, 0)
    print(max(color))
    for c in color:
        print(c)
