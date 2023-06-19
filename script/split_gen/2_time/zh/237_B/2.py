def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            if j == H - 1:
                print(A[j][i])
            else:
                print(A[j][i], end=' ')
