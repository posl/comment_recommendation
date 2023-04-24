Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    #N, M, Q = 2, 3, 1
    #LR = [[1, 1], [1, 2], [2, 2]]
    #PQ = [[1, 2]]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    LR.sort()
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    for i in range(Q):
        #print(PQ[i])
        #print()
        #print(LR)
        #print(PQ[i])
        #print()
        #print(LR[0][0])
        #print(PQ[i][0])
        #print()
        #print(LR[0][1])
        #print(PQ[i][1])
        #print()
        #print()
        #print()
        print(sum([1 for j in range(M) if LR[j][0] <= PQ[i][0] and LR[j][1] >= PQ[i][1]]))

=======
Suggestion 2

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
        ans = 0
        for j in range(M):
            if P[i] <= L[j] and R[j] <= Q[i]:
                ans += 1
        print(ans)

=======
Suggestion 3

def main():
    N,M,Q = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(M)]
    PQ = [list(map(int,input().split())) for _ in range(Q)]
    #p

=======
Suggestion 4

def main():
    n,m,q = map(int,input().split())
    l = [0] * m
    r = [0] * m
    p = [0] * q
    q = [0] * q
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        cnt = 0
        for j in range(m):
            if p[i] <= l[j] and r[j] <= q[i]:
                cnt += 1
        print(cnt)

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    n, m, q = map(int, input().split())
    trains = []
    for _ in range(m):
        l, r = map(int, input().split())
        trains.append((l, r))
    trains.sort()
    #print(trains)
    for _ in range(q):
        p, q = map(int, input().split())
        cnt = 0
        for train in trains:
            if p <= train[0] and train[1] <= q:
                cnt += 1
        print(cnt)

=======
Suggestion 7

def solve():
    N,M,Q = map(int, input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int, input().split())
    p = [0]*Q
    q = [0]*Q
    for i in range(Q):
        p[i],q[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(M):
            if p[i] <= L[j] and R[j] <= q[i]:
                count += 1
        print(count)
    return 0

=======
Suggestion 8

def main():
    N,M,Q = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(M)]
    PQ = [list(map(int,input().split())) for _ in range(Q)]
    LR.sort()
    PQ.sort()
    LR = [[l,r] for l,r in LR]
    PQ = [[p,q] for p,q in PQ]
    #print(LR)
    #print(PQ)
    for p,q in PQ:
        count = 0
        for l,r in LR:
            if p <= l and r <= q:
                count += 1
        print(count)

=======
Suggestion 9

def get_input_data():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    return n, m, q, lr, pq

=======
Suggestion 10

def main():
    n,m,q = map(int,input().split())
    train = [0]*n
    for i in range(m):
        l,r = map(int,input().split())
        for j in range(l-1,r):
            train[j] += 1
    for i in range(q):
        p,q = map(int,input().split())
        count = 0
        for j in range(p-1,q):
            count += train[j]
        print(count)
main()
