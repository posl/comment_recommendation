def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        ans[v] = ans[p] + G[v][p][1]
        for i, (nv, w) in enumerate(G[v]):
            if nv == p:
                continue
            stack.append((nv, v))
    for i in range(N):
        print(ans[i] % 2)
