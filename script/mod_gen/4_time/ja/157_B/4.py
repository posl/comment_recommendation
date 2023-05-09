def judge_bingo():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
    if (A[0][0] == 0 and A[0][1] == 0 and A[0][2] == 0) or (A[1][0] == 0 and A[1][1] == 0 and A[1][2] == 0) or (A[2][0] == 0 and A[2][1] == 0 and A[2][2] == 0) or (A[0][0] == 0 and A[1][0] == 0 and A[2][0] == 0) or (A[0][1] == 0 and A[1][1] == 0 and A[2][1] == 0) or (A[0][2] == 0 and A[1][2] == 0 and A[2][2] == 0) or (A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0) or (A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    judge_bingo()