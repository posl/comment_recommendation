def is_contradictory(N, A):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return True
            if A[i][j] == 'L' and A[j][i] != 'W':
                return True
            if A[i][j] == 'D' and A[j][i] != 'D':
                return True
    return False
N = int(input())
A = [input() for _ in range(N)]
