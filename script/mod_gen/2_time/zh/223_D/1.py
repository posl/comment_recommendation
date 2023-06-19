def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
    ans = []
    from collections import deque
    q = deque()
    for i in range(n):
        if not g[i]:
            q.append(i)
    while q:
        v = q.popleft()
        ans.append(v)
        for i in range(n):
            if v in g[i]:
                g[i].remove(v)
                if not g[i]:
                    q.append(i)
    if len(ans) != n:
        print(-1)
    else:
        print(*[x+1 for x in ans])
solve()
