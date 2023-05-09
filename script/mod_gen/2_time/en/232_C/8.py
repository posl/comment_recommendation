def isSameShape(N,M,A,B,C,D):
    for i in range(N):
        for j in range(i+1,N):
            if (A[i] in C[j] and A[j] in C[i]) or (A[i] in D[j] and A[j] in D[i]):
                continue
            else:
                return False
    return True

if __name__ == '__main__':
    isSameShape()