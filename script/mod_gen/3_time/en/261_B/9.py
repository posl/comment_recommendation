def check(A):
    for i in range(len(A)):
        if A[i][i] != '-':
            return False
        for j in range(len(A)):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return False
            if A[i][j] == 'L' and A[j][i] != 'W':
                return False
            if A[i][j] == 'D' and A[j][i] != 'D':
                return False
    return True
N = int(input())
A = [input() for _ in range(N)]

if __name__ == '__main__':
    check()