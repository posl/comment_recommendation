def stamp(N,M,A):
    if M==0:
        return 1
    else:
        A.sort()
        if A[0]!=1:
            A.insert(0,0)
        if A[-1]!=N:
            A.append(N+1)
        B=[]
        for i in range(1,len(A)):
            if A[i]-A[i-1]-1>0:
                B.append(A[i]-A[i-1]-1)
        return min(B)

if __name__ == '__main__':
    stamp()