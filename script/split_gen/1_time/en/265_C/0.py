def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if G[i][j] == "R":
            j += 1
        elif G[i][j] == "L":
            j -= 1
        elif G[i][j] == "U":
            i -= 1
        else:
            i += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return
    print(-1)
