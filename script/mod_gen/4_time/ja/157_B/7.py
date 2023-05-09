def check_bingo(A):
    # check rows
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2]:
            return True
    # check columns
    for i in range(3):
        if A[0][i] == A[1][i] == A[2][i]:
            return True
    # check diagonal
    if A[0][0] == A[1][1] == A[2][2]:
        return True
    if A[0][2] == A[1][1] == A[2][0]:
        return True
    return False

if __name__ == '__main__':
    check_bingo()