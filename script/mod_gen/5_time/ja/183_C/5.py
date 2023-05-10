def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, i, K, T, N)
    print(ans)

if __name__ == '__main__':
    main()