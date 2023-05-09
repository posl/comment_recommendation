def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import deque
    readline = stdin.readline
    N, M = map(int, readline().split())
    bridge = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, readline().split())
        bridge[a].append(b)
        bridge[b].append(a)
    for i in range(1, N+1):
        bridge[i].sort()
    visited = [False] * (N+1)
    visited[1] = True
    q = deque([1])
    count = 0
    while q:
        v = q.popleft()
        for w in bridge[v]:
            if not visited[w]:
                visited[w] = True
                count += 1
                q.append(w)
    print(M - count)
