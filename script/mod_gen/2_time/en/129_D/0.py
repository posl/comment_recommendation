def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            ans = max(ans, bfs(i, j, S))
    print(ans)

if __name__ == '__main__':
    main()