def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    def dfs(cur, visited, cost):
        if len(visited) == N:
            if cost + T[cur][0] == K:
                return 1
            else:
                return 0
        res = 0
        for i in range(N):
            if i not in visited:
                res += dfs(i, visited + [i], cost + T[cur][i])
        return res
    print(dfs(0, [0], 0))
