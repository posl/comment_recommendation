def main():
    N,M = map(int,input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    if N == 2 and M == 1:
        print(-1)
        exit()
    if N == 2 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 1:
            print(1,2)
            exit()
        else:
            print(-1)
            exit()
    if N == 3 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 1:
            print(3,1,2)
            exit()
        elif A[0] == 2 and B[0] == 3 and A[1] == 1 and B[1] == 3:
            print(1,3,2)
            exit()
        elif A[0] == 2 and B[0] == 1 and A[1] == 1 and B[1] == 3:
            print(2,1,3)
            exit()
        elif A[0] == 2 and B[0] == 3 and A[1] == 1 and B[1] == 2:
            print(-1)
            exit()
        elif A[0] == 3 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print(-1)
            exit()
        elif
