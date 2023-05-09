def check_win(i,j):
    if A[i][j] == 'W':
        if A[j][i] != 'L':
            return False
    elif A[i][j] == 'L':
        if A[j][i] != 'W':
            return False
    else:
        if A[j][i] != 'D':
            return False
    return True
N = int(input())
A = []
for i in range(N):
    A.append(input())
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if not check_win(i,j):
            print('incorrect')
            exit()
print('correct')
