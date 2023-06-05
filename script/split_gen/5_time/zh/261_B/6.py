def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] == 'W' or A[j][i] == 'D':
                    print('不正确')
                    return
            elif A[i][j] == 'L':
                if A[j][i] == 'L' or A[j][i] == 'D':
                    print('不正确')
                    return
            elif A[i][j] == 'D':
                if A[j][i] == 'W' or A[j][i] == 'L':
                    print('不正确')
                    return
    print('正确')
