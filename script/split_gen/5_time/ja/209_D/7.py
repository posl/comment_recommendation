def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        dist = [-1] * n
        dist[c] = 0
        stack = [c]
        while stack:
            v = stack.pop()
            for u in tree[v]:
                if dist[u] != -1:
                    continue
                dist[u] = dist[v] + 1
                stack.append(u)
        if dist[d] % 2 == 0:
            print('Town')
        else:
            print('Road')
