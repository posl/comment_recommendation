def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u-1].append((v-1, w))
        adj[v-1].append((u-1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for nxt, w in adj[now]:
            if color[nxt] == -1:
                color[nxt] = color[now] ^ (w%2)
                stack.append(nxt)
    for c in color:
        print(c)
