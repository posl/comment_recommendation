def solve():
    from sys import stdin
    readline = stdin.readline
    N, M, K = map(int, readline().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    for _ in range(K):
        c, d = map(int, readline().split())
        c -= 1
        d -= 1
        blocks[c].add(d)
        blocks[d].add(c)
    # dfs
    def dfs(v, seen):
        seen.add(v)
        for u in friends[v]:
            if u not in seen and u not in blocks[v]:
                dfs(u, seen)
        return seen
    ans = [0] * N
    for i in range(N):
        ans[i] = len(dfs(i, set())) - len(friends[i]) - 1
    print(*ans)
