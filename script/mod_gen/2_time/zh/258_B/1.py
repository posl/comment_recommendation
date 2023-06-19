def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                ans = max(ans, dfs(a, i, j, n))
    print(ans)

if __name__ == '__main__':
    main()