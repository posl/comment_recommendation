def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    #print(N, K, T)
    cnt = 0
    for i in range(1, N):
        cnt += dfs(i, N, K, T, 0)
    print(cnt)
