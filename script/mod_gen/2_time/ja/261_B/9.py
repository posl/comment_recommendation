def check_result():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))
    #print(A)
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W' and A[j][i] != 'L':
                return False
            if A[i][j] == 'L' and A[j][i] != 'W':
                return False
            if A[i][j] == 'D' and A[j][i] != 'D':
                return False
    return True
print('correct' if check_result() else 'incorrect')

if __name__ == '__main__':
    check_result()