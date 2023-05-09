def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))
    color = [-1] * n
    color[0] = 0
    que = [0]
    while que:
        q = que.pop()
        for v, w in edge[q]:
            if color[v] == -1:
                color[v] = color[q] ^ (w % 2)
                que.append(v)
    for c in color:
        print(c)
