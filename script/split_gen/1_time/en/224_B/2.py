def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                A[i][j] += A[i][j-1]
            elif j == 0:
                A[i][j] += A[i-1][j]
            else:
                A[i][j] += max(A[i][j-1], A[i-1][j])
    print('Yes' if A[H-1][W-1] % 2 == 0 else 'No')
