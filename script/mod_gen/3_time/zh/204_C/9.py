def solve(n, m, ab):
    # 从一个点出发，最多能到达的点数
    def dfs(start):
        visited = [False] * (n + 1)
        visited[start] = True
        stack = [start]
        while stack:
            v = stack.pop()
            for u in ab[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        return sum(visited)
    # 按照题意，从1~n每个点出发，能到达的点数
    ans = 0
    for i in range(1, n + 1):
        ans += dfs(i)
    return ans

if __name__ == '__main__':
    solve()