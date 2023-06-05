def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, i, N, K, T)
    print(ans)
