def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    from collections import deque
    dist = [-1]*N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in edge[v]:
            if dist[nv] != -1: continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    for _ in range(Q):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if dist[c]%2 == dist[d]%2:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()