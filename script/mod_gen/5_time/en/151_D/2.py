def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(ans, bfs(H, W, S, i, j))
    print(ans)

if __name__ == '__main__':
    main()