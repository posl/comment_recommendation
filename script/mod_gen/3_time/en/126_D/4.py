def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    Q = deque([0])
    visited = [False] * N
    d = [0] * N
    while Q:
        v = Q.popleft()
        visited[v] = True
        for nv, w in G[v]:
            if visited[nv]:
                continue
            d[nv] = d[v] + w
            Q.append(nv)
    for i in range(N):
        if d[i] % 2 == 0:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    main()