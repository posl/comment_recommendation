def dfs(now, visited, cost, n, k, t):
    visited[now] = True
    if all(visited):
        return cost + t[now][0] == k
    else:
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += dfs(i, visited, cost + t[now][i], n, k, t)
        return ans
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
print(dfs(0, visited, 0, n, k, t))

if __name__ == '__main__':
    dfs()