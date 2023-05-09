def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    def dfs(v, k, visited):
        if k == 0 and v == 0:
            return 1
        if k < 0 or v == 0:
            return 0
        res = 0
        for i in range(n):
            if visited & 1 << i == 0:
                res += dfs(i, k - t[v][i], visited | 1 << i)
        return res
    print(dfs(0, k, 1 << 0))
