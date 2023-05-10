def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1 for j in range(W)] for i in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while len(q) > 0:
        i, j = q.pop(0)
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if 0 <= i2 < H and 0 <= j2 < W and S[i2][j2] == "." and dist[i2][j2] == -1:
                    dist[i2][j2] = dist[i][j] + 1
                    q.append((i2, j2))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()