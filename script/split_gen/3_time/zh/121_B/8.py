def is_correct(A,B,C):
    ans = 0
    for i in range(len(A)):
        ans += A[i]*B[i]
    ans += C
    if ans > 0:
        return True
    else:
        return False
