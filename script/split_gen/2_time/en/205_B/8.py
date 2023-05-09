def check_permutation(N, A):
    #print("N: ", N)
    #print("A: ", A)
    A.sort()
    #print("A: ", A)
    for i in range(N):
        if A[i] != i+1:
            return False
    return True
