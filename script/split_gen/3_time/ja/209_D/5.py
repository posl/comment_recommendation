def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    dist = [0] * N
    que = deque([0])
    while que:
        p = que.popleft()
        for c in edges[p]:
            if dist[c] == 0:
                dist[c] = dist[p] + 1
                que.append(c)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")
