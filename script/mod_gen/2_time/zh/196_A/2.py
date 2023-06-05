def main():
    N,M,Q=map(int,input().split())
    W=[]
    V=[]
    for i in range(N):
        w,v=map(int,input().split())
        W.append(w)
        V.append(v)
    X=list(map(int,input().split()))
    for i in range(Q):
        L,R=map(int,input().split())
        X1=X[:L-1]
        X2=X[R:]
        X1.extend(X2)
        X1.sort()
        ans=0
        for j in range(N):
            for k in range(len(X1)):
                if W[j]<=X1[k]:
                    ans+=V[j]
                    X1.remove(X1[k])
                    break
        print(ans)
main()
