def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                ans = max(ans, dfs(i, j, s, h, w))
    print(ans)

if __name__ == '__main__':
    main()