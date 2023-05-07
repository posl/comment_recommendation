def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x1, y1 = i, j
            elif S[i][j] == 'o':
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))
