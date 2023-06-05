def find_second_place(N, A):
    #print(N, A)
    #print(len(A))
    if N == 1:
        if A[0] > A[1]:
            return 2
        else:
            return 1
    else:
        N = N - 1
        A1 = A[:2**N]
        A2 = A[2**N:]
        A1.sort()
        A2.sort()
        #print(A1)
        #print(A2)
        if A1[-1] > A2[-1]:
            A2[-1] = A1[-1]
            return find_second_place(N, A2)
        else:
            A1[-1] = A2[-1]
            return find_second_place(N, A1)
