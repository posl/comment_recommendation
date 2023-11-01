def check():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif A[i][j] == 'W' and A[j][i] != 'L':
                return 'incorrect'
            elif A[i][j] == 'L' and A[j][i] != 'W':
                return 'incorrect'
            elif A[i][j] == 'D' and A[j][
