def resolve():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))
    ans = []
    q = deque([0])
    seen = [False] * N
    while q:
        u = q.popleft()
        ans.append(u+1)
        seen[u] = True
        for v, i in G[u]:
            if seen[v]:
                continue
            q.append(v)
            ans.append(u+1)
    print(*ans)

if __name__ == '__main__':
    resolve()