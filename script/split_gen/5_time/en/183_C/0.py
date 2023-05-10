def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, t, k, 0)
    print(ans)
