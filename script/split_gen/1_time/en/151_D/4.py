def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    max_path = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                max_path = max(max_path, bfs(H, W, S, i, j))
    print(max_path)
