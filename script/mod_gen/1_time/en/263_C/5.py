def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        dfs(i, n - 1, m)

if __name__ == '__main__':
    main()