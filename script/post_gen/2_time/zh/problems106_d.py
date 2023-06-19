Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(Q):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)
    for i in range(Q):
        count = 0
        for j in range(M):
            if L[j] >= P[i] and R[j] <= Q[i]:
                count += 1
        print(count)
main()

=======
Suggestion 2

def read_data():
    line1 = input().split()
    N = int(line1[0])
    M = int(line1[1])
    Q = int(line1[2])
    trains = []
    for i in range(M):
        line = input().split()
        trains.append((int(line[0]), int(line[1])))
    queries = []
    for i in range(Q):
        line = input().split()
        queries.append((int(line[0]), int(line[1])))
    return N, M, Q, trains, queries

=======
Suggestion 3

def get_data():
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

=======
Suggestion 4

def main():
    N,M,Q = map(int,input().split())
    trains = []
    for i in range(M):
        trains.append(list(map(int,input().split())))
    for i in range(Q):
        p,q = map(int,input().split())
        count = 0
        for j in range(M):
            if trains[j][0] >= p and trains[j][1] <= q:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    n, m, q = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    p = [0] * q
    q = [0] * q
    for i in range(q):
        p[i], q[i] = map(int, input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i] <= l[j] and r[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    trains = [[0 for i in range(N+1)] for j in range(M+1)]
    for i in range(M):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            trains[i][j] = 1
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(p, q+1):
            for k in range(M):
                if trains[k][j] == 1:
                    count += 1
                    break
        print(count)

=======
Suggestion 7

def problem106_d():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        L, R = map(int, input().split())
        LR.append((L, R))
    PQ = []
    for i in range(Q):
        P, Q = map(int, input().split())
        PQ.append((P, Q))
    ans = [0] * Q
    for i in range(M):
        for j in range(Q):
            if LR[i][0] <= PQ[j][0] and LR[i][1] >= PQ[j][1]:
                ans[j] += 1
    for i in range(Q):
        print(ans[i])

problem106_d()

=======
Suggestion 8

def readData():
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

=======
Suggestion 9

def main():
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

    #print(N,M,Q,L,R,P,Q)
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(L[1],R[1],P[1],Q[1])
    #print(L[2],R[2],P[2],Q[2])

    #print(L[0],R[0],P[0],Q[0])
    #print(L[1],R[1],P[1],Q[1])
    #print(L[2],R[2],P[2],Q[2])
    #print(L[3],R[3],P[3],Q[3])
    #print(L[4],R[4],P[4],Q[4])
    #print(L[5],R[5],P[5],Q[5])
    #print(L[6],R[6],P[6],Q[6])
    #print(L[7],R[7],P[7],Q[7])
    #print(L[8],R[8],P[8],Q[8])
    #print(L[9],R[9],P[9],Q[9])
    #print(L[10],R[10],P[10],Q[10])
    #print(L[11],R[11],P[11],Q[11])
    #print(L[12],R[12],P[12],Q[12])
    #print(L[13],R[13],P[13],Q[13])
    #print(L[14],R[14],P[14],Q[14])
    #print(L[15],R[15],P[15],Q[15])
    #print(L[16],R[16],P[16],Q[16])
    #print(L[17],R[17],

=======
Suggestion 10

def main():
    n,m,q = map(int, input().split())
    trains = []
    for _ in range(m):
        l,r = map(int, input().split())
        trains.append((l,r))
    for _ in range(q):
        p,q = map(int, input().split())
        count = 0
        for l,r in trains:
            if p <= l and r <= q:
                count += 1
        print(count)
