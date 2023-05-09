def main():
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    X=[int(input()) for i in range(q)]
    #print(A,X)
    for i in range(q):
        #print(X[i])
        #print(A)
        count=0
        for j in range(n):
            if X[i]==A[j]:
                continue
            elif X[i]<A[j]:
                count+=A[j]-X[i]
            else:
                count+=X[i]-A[j]
        print(count)
