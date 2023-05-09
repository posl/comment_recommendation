def main():
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        g[u-1].append((v-1, w))
        g[v-1].append((u-1, w))
    color = [-1]*N
    color[0] = 0
    stack = [0]
    while stack:
        p = stack.pop()
        for q, w in g[p]:
            if color[q] == -1:
                color[q] = color[p] ^ (w%2)
                stack.append(q)
    for i in range(N):
        print(color[i])
