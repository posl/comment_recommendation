def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, bfs(h, w, H, W, S))
    print(ans)

if __name__ == '__main__':
    main()