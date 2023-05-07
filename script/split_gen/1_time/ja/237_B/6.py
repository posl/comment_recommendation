def main():
    #入力
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #転置行列
    B = [[0 for i in range(H)] for j in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    #出力
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print()
