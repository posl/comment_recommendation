def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # print(H, W, C)
    # print(A)
    # print()
    minA = [[float('inf') for _ in range(W)] for _ in range(H)]
    minB = [[float('inf') for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                minA[i][j] = A[i][j]
            elif i == 0:
                minA[i][j] = min(minA[i][j-1], A[i][j])
            elif j == 0:
                minA[i][j] = min(minA[i-1][j], A[i][j])
            else:
                minA[i][j] = min(minA[i-1][j], minA[i][j-1], A[i][j])
    # print(minA)
    # print()
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                minB[i][j] = A[i][j]
            elif i == H-1:
                minB[i][j] = min(minB[i][j+1], A[i][j])
            elif j == W-1:
                minB[i][j] = min(minB[i+1][j], A[i][j])
            else:
                minB[i][j] = min(minB[i+1][j], minB[i][j+1], A[i][j])
    # print(minB)
    # print()
    minCost = float('inf')
    for i in range(H):
        for j in range(W):
            minCost = min(minCost, minA[i][j] + minB[i][j] + C*(i+j))
    print(minCost)
