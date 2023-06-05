def count_chessboard(H, W, S):
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    return count

if __name__ == '__main__':
    count_chessboard()