def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                y1, x1 = i, j
            if S[i][j] == 'o':
                y2, x2 = i, j
    print(abs(x1 - x2) + abs(y1 - y2))
