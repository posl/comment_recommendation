def solve():
    n, m = map(int, input().split())
    if m == 0:
        print(n)
        return
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
    ans = 0
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        stack = [i]
        while stack:
            now = stack.pop()
            for next in edge[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
        ans += sum(visited)
    print(ans)

if __name__ == '__main__':
    solve()