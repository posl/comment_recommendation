def main():
    H, W = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(H)]
    N = 0
    moves = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    moves.append((i + 1, j + 1, i + 1, j + 2))
                    N += 1
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    moves.append((i + 1, j + 1, i + 2, j + 1))
                    N += 1
    print(N)
    for move in moves:
        print(*move)
