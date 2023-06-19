def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for i in range(H)]
    C_h, C_w, D_h, D_w = C_h - 1, C_w - 1, D_h - 1, D_w - 1
    D = [[-1] * W for i in range(H)]
    D[C_h][C_w] = 0
    Q = [(C_h, C_w)]
    while len(Q) > 0:
        i, j = Q.pop(0)
        for i2 in range(max(0, i - 2), min(H, i + 3)):
            for j2 in range(max(0, j - 2), min(W, j + 3)):
                if S[i2][j2] == '.' and D[i2][j2] == -1:
                    D[i2][j2] = D[i][j] + 1
                    Q.append((i2, j2))
    print(D[D_h][D_w])
