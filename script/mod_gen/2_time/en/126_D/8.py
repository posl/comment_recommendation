def main():
    import sys
    from collections import deque
    sys.setrecursionlimit(10 ** 7)
    n = int(input())
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges[u - 1].append((v - 1, w))
        edges[v - 1].append((u - 1, w))
    colors = [-1] * n
    colors[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv, w in edges[v]:
            if colors[nv] != -1:
                continue
            if w % 2 == 0:
                colors[nv] = colors[v]
            else:
                colors[nv] = 1 - colors[v]
            q.append(nv)
    for c in colors:
        print(c)

if __name__ == '__main__':
    main()