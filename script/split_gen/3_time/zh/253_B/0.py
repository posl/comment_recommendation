def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    l = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                l.append((i, j))
    x1, y1 = l[0]
    x2, y2 = l[1]
    print(max(abs(x1 - x2), abs(y1 - y2)) + 1)
