def min_time():
    #N = int(input())
    N = 3
    #A = []
    #B = []
    #for i in range(N):
    #    A_i, B_i = map(int, input().split())
    #    A.append(A_i)
    #    B.append(B_i)
    A = [8, 4, 7]
    B = [5, 4, 9]
    min_time = 0
    for i in range(N):
        if A[i] > B[i]:
            min_time += A[i]
        else:
            min_time += B[i]
    print(min_time)
