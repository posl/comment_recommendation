def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (color[v] + w) % 2
                stack.append(nv)
    print(*color, sep='
')
