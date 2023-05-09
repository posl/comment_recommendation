def main():
    n, k = map(int, input().split())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, 1, n, k, t)
    print(ans)

if __name__ == '__main__':
    main()