def main():
    N,M,Q = map(int,input().split())
    L = [0]*M
    R = [0]*M
    p = [0]*Q
    q = [0]*Q
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    for i in range(Q):
        p[i],q[i] = map(int,input().split())
    #print(N,M,Q,L,R,p,q)
    for i in range(Q):
        cnt = 0
        for j in range(M):
            if p[i]<=L[j] and R[j]<=q[i]:
                cnt+=1
        print(cnt)
