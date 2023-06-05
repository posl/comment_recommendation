def is_correct(A):
    for i in range(len(A)):
        for j in range(len(A)):
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
N = int(input())
A = [list(input()) for i in range(N)]
print('正确' if is_correct(A) else '不正确')
