def main():
    N,M = map(int,input().split())
    #print(N,M)
    #A = []
    #B = []
    #for i in range(M):
    #    a,b = map(int,input().split())
    #    A.append(a)
    #    B.append(b)
    #print(A)
    #print(B)
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    #A = [1,2,3,4,5]
    #B = [1,2,3,4,5]
    Acount = 0
    Bcount = 0
    Acountmax = 0
    Bcountmax = 0
    for i in range(N-1):
        #print(i)
        #print(Acount)
        #print(Bcount)
        if A[Acount] == i+1:
            Acount += 1
        if B[Bcount] == i+1:
            Bcount += 1
        Acountmax = max(Acountmax,Acount)
        Bcountmax = max(Bcountmax,Bcount)
    #print(Acountmax)
    #print(Bcountmax)
    if Acountmax + Bcountmax >= M:
        print(M-(Acountmax+Bcountmax))
    else:
        print(M-(Acountmax+Bcountmax)+1)

if __name__ == '__main__':
    main()