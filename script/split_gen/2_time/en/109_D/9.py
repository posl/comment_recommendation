def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # N: number of operations
    N = 0
    # ops: operations
    ops = []
    # for each row
    for i in range(H):
        # for each column
        for j in range(W):
            # if the number of coins is odd
            if A[i][j] % 2 == 1:
                # if the cell is not the last cell in the row
                if j < W - 1:
                    # move one coin to the right
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    N += 1
                    ops.append((i + 1, j + 1, i + 1, j + 2))
                # if the cell is the last cell in the row
                else:
                    # move one coin to the bottom
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    N += 1
                    ops.append((i + 1, j + 1, i + 2, j + 1))
    # output
    print(N)
    for op in ops:
        print(*op)
