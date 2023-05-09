def main():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
    if A[0][0] == A[0][1] == A[0][2] == 0 or A[1][0] == A[1][1] == A[1][2] == 0 or A[2][0] == A[2][1] == A[2][2] == 0 or A[0][0] == A[1][0] == A[2][0] == 0 or A[0][1] == A[1][1] == A[2][1] == 0 or A[0][2] == A[1][2] == A[2][2] == 0 or A[0][0] == A[1][1] == A[2][2] == 0 or A[0][2] == A[1][1] == A[2][0] == 0:
        print('Yes')
    else:
        print('No')
