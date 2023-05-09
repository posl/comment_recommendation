def main():
    N = int(input())
    A = [input() for i in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    flag = False
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    flag = False
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    flag = False
    if flag:
        print('correct')
    else:
        print('incorrect')
