def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    black = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                black += 1
    if black == 1:
        print(1)
        return
    if black == H * W:
        print(H * W)
        return
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                    print(2)
                    return
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 1 or i == H - 2 or j == 1 or j == W - 2:
                    print(3)
                    return
    print(4)
    return
