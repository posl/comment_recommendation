def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [input() for _ in range(H)]
    C = [[-1]*W for _ in range(H)]
    C[Ch-1][Cw-1] = 0
    Q = [(Ch-1, Cw-1)]
    while Q:
        h, w = Q.pop()
        if h < H-1 and S[h+1][w] == "." and C[h+1][w] == -1:
            C[h+1][w] = C[h][w]
            Q.append((h+1, w))
        if h > 0 and S[h-1][w] == "." and C[h-1][w] == -1:
            C[h-1][w] = C[h][w]
            Q.append((h-1, w))
        if w < W-1 and S[h][w+1] == "." and C[h][w+1] == -1:
            C[h][w+1] = C[h][w]
            Q.append((h, w+1))
        if w > 0 and S[h][w-1] == "." and C[h][w-1] == -1:
            C[h][w-1] = C[h][w]
            Q.append((h, w-1))
        for i in range(-2, 3):
            for j in range(-2, 3):
                if h+i < 0 or h+i >= H or w+j < 0 or w+j >= W or S[h+i][w+j] == "#":
                    continue
                if C[h+i][w+j] == -1:
                    C[h+i][w+j] = C[h][w]+1
                    Q.append((h+i, w+j))
    print(C[Dh-1][Dw-1])
