def main():
    # input
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # compute
    B = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            B[i][j] = A[i][j] - C*(i+j)
    # output
    print(min([min(B[i]) for i in range(H)]))
