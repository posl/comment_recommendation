def judge(H, N, A):
    #print(H, N, A)
    if H == 0:
        return True
    if H < 0:
        return False
    if N == 0:
        return False
    if judge(H-A[0], N-1, A[1:]) or judge(H, N-1, A[1:]):
        return True
    else:
        return False
