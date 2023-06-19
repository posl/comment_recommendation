def find_num(A,L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count
