def min_operations(N, A):
    #print(N, A)
    if N == 1:
        return 0
    else:
        A = list(A)
        #print(A)
        count = 0
        for i in range(0, N//2):
            #print(i, N-1-i)
            if A[i] != A[N-1-i]:
                count += 1
                #print(count)
        return count
