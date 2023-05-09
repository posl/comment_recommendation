def is_correct(N, A):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    return False
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    return False
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    return False
    return True
