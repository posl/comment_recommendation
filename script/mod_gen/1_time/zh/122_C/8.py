def solve():
    N,Q = map(int,input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_,r_ = map(int,input().split())
        l.append(l_)
        r.append(r_)
    #print(N,Q,S,l,r)
    #print(S[2:7])
    #print(S.count("AC",2,7))
    #print(S[1:3])
    #print(S.count("AC",1,3))
    #print(S[0:8])
    #print(S.count("AC",0,8))
    for i in range(Q):
        print(S.count("AC",l[i]-1,r[i]))

if __name__ == '__main__':
    solve()