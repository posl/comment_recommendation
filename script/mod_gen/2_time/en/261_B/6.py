def check(A):
    N = len(A)
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    return False
            else:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    return False
                if A[i][j] == 'L' and A[j][i] != 'W':
                    return False
                if A[i][j] == 'D' and A[j][i] != 'D':
                    return False
    return True
N = int(input())
A = []
for i in range(N):
    A.append(input())

if __name__ == '__main__':
    check()