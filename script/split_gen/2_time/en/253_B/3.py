def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x1 = i
                y1 = j
            if S[i][j] == 'o':
                x2 = i
                y2 = j
    print(abs(x1-x2) + abs(y1-y2))
