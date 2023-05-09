def main():
    H, W = map(int, input().split())
    A = [input().split() for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print()
