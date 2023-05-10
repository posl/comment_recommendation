def main():
    N, Q = map(int, input().split())
    tree = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].add(b-1)
        tree[b-1].add(a-1)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        from collections import deque
        que = deque()
        que.append((c, 0))
        dist = [-1] * N
        while que:
            v, d = que.popleft()
            dist[v] = d
            for u in tree[v]:
                if dist[u] == -1:
                    que.append((u, d+1))
        if dist[d] % 2 == 0:
            print("Town")
        else:
            print("Road")
