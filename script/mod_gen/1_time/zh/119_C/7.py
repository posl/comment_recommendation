def getMinMP(N,A,B,C,l):
    #print("N,A,B,C,l:",N,A,B,C,l)
    if N==0:
        if A==0 and B==0 and C==0:
            return 0
        else:
            return 1000000
    if A==0 and B==0 and C==0:
        return 0
    if A<0 or B<0 or C<0:
        return 1000000
    if A==0 and B==0 and C==0:
        return 0
    if l[0]==A or l[0]==B or l[0]==C:
        return getMinMP(N-1,A-l[0],B,C,l[1:])
    else:
        return min(getMinMP(N-1,A,B,C,l[1:]),1+getMinMP(N-1,A-l[0],B,C,l[1:]),1+getMinMP(N-1,A,B-l[0],C,l[1:]),1+getMinMP(N-1,A,B,C-l[0],l[1:]))
N,A,B,C=map(int,input().split())
l=[]
for i in range(N):
    l.append(int(input()))
print(getMinMP(N,A,B,C,l))
