def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    res = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                        res += 1
    print(res//2)
