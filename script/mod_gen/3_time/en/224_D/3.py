def main():
    from sys import stdin
    from collections import deque
    readline = stdin.readline
    M = int(readline())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, readline().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    P = [int(x)-1 for x in readline().split()]
    Q = deque([P])
    visited = set()
    while Q:
        p = Q.popleft()
        if p in visited:
            continue
        visited.add(tuple(p))
        for i in range(8):
            if p[i] == i:
                continue
            for j in range(8):
                if p[j] == i:
                    break
            for v in G[p[i]]:
                if v == p[j]:
                    q = p[:]
                    q[i], q[j] = q[j], q[i]
                    Q.append(q)
    if (0, 1, 2, 3, 4, 5, 6, 7) in visited:
        print(len(visited) - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()