def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, dfs(h, w, S))
    print(ans)
