def main():
    N,M,Q = map(int,input().split())
    #print(N,M,Q)
    #print(type(N),type(M),type(Q))
    #L = [0]*M
    #R = [0]*M
    #P = [0]*Q
    #Q = [0]*Q
    #for i in range(M):
    #    L[i],R[i] = map(int,input().split())
    #for i in range(Q):
    #    P[i],Q[i] = map(int,input().split())
    #print(L,R,P,Q)
    #print(type(L),type(R),type(P),type(Q))
    L = []
    R = []
    P = []
    Q = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    for i in range(Q):
        p,q = map(int,input().split())
        P.append(p)
        Q.append(q)
    #print(L,R,P,Q)
    #print(type(L),type(R),type(P),type(Q))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[
