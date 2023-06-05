def get_input():
    #获取输入
    N,M,Q = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(Q):
        p,q = map(int,input().split())
        P.append(p)
        Q.append(q)
    return N,M,Q,L,R,P,Q

if __name__ == '__main__':
    get_input()