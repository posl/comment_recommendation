def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        u, c = stack.pop()
        for v, w in G[u]:
            if color[v] == -1:
                color[v] = (c + w) % 2
                stack.append((v, color[v]))
    for c in color:
        print(c)
