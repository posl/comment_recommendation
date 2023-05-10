def main():
    N,K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    ans = 0
    for i in range(1,N):
        ans += dfs(i, 1<<i, T, K)
    print(ans)

if __name__ == '__main__':
    main()