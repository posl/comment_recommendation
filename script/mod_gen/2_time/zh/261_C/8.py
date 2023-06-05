def check(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 'W' and A[j][i] != 'L':
                return False
            if A[i][j] == 'L' and A[j][i] != 'W':
                return False
            if A[i][j] == 'D' and A[j][i] != 'D':
                return False
    return True

if __name__ == '__main__':
    check()