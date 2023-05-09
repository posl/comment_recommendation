def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for v in range(n):
        for u in graph[v]:
            for w in graph[u]:
                if w == v: continue
                if v in graph[w]:
                    ans += 1
    print(ans//6)

if __name__ == '__main__':
    solve()