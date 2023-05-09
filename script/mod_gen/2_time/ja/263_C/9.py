def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        dfs(i, N, M)

if __name__ == '__main__':
    main()