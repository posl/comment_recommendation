Synthesizing 10/10 solutions

=======
Suggestion 1

def count_train(l, r, trains):
    cnt = 0
    for train in trains:
        if l <= train[0] and train[1] <= r:
            cnt += 1
    return cnt

=======
Suggestion 2

def solve():
    N,M,Q = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(M)]
    PQ = [list(map(int,input().split())) for _ in range(Q)]

    LR.sort(key=lambda x:x[1])

    for p,q in PQ:
        ans = 0
        for l,r in LR:
            if p<=l and r<=q:
                ans += 1
        print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        l, r = map(int, input().split())
        LR.append((l, r))
    PQ = []
    for i in range(Q):
        p, q = map(int, input().split())
        PQ.append((p, q))
    for i in range(Q):
        ans = 0
        for j in range(M):
            if LR[j][0] >= PQ[i][0] and LR[j][1] <= PQ[i][1]:
                ans += 1
        print(ans)

=======
Suggestion 4

def main():
    n,m,q = map(int,input().split())
    lr = [list(map(int,input().split())) for _ in range(m)]
    pq = [list(map(int,input().split())) for _ in range(q)]
    #print(n,m,q,lr,pq)
    #print(lr[0][1])
    #print(pq[0][1])
    #print(lr[0][0] <= pq[0][0])
    #print(lr[0][1] >= pq[0][1])
    #print(lr[0][0] <= pq[0][0] and lr[0][1] >= pq[0][1])
    #print(lr[0][0] <= pq[0][0] and lr[0][1] >= pq[0][1])
    #print(lr[1][0] <= pq[0][0] and lr[1][1] >= pq[0][1])
    #print(lr[2][0] <= pq[0][0] and lr[2][1] >= pq[0][1])
    #print(lr[0][0] <= pq[1][0] and lr[0][1] >= pq[1][1])
    #print(lr[1][0] <= pq[1][0] and lr[1][1] >= pq[1][1])
    #print(lr[2][0] <= pq[1][0] and lr[2][1] >= pq[1][1])
    #print(lr[0][0] <= pq[2][0] and lr[0][1] >= pq[2][1])
    #print(lr[1][0] <= pq[2][0] and lr[1][1] >= pq[2][1])
    #print(lr[2][0] <= pq[2][0] and lr[2][1] >= pq[2][1])
    #print(lr[0][0] <= pq[3][0] and lr[0][1] >= pq[3][1])
    #print(lr[1][0] <= pq[3][0] and lr[1][1] >= pq[3][1])
    #print(lr[2][0] <= pq[3][0] and lr[2][1] >= pq[3][1])

=======
Suggestion 5

def count_trains(start, end, trains):
    count = 0
    for train in trains:
        if train[0] >= start and train[1] <= end:
            count += 1
    return count

=======
Suggestion 6

def main():
    N,M,Q = map(int,input().split())
    train = []
    for i in range(M):
        L,R = map(int,input().split())
        train.append([L,R])
    train.sort()
    for i in range(Q):
        p,q = map(int,input().split())
        ans = 0
        for j in range(M):
            if p <= train[j][0] and train[j][1] <= q:
                ans += 1
        print(ans)

=======
Suggestion 7

def get_data():
    n,m,q = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    p = []
    q = []
    for i in range(q):
        p_i,q_i = map(int,input().split())
        p.append(p_i)
        q.append(q_i)
    return n,m,q,l,r,p,q

=======
Suggestion 8

def get_input():
    n, m, q = map(int, input().split())
    l_r = [list(map(int, input().split())) for _ in range(m)]
    p_q = [list(map(int, input().split())) for _ in range(q)]
    return n, m, q, l_r, p_q

=======
Suggestion 9

def main():
    n,m,q = map(int,input().split())
    l = [0]*m
    r = [0]*m
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    p = [0]*q
    q = [0]*q
    for i in range(q):
        p[i],q[i] = map(int,input().split())

=======
Suggestion 10

def main():
    N,M,Q = map(int,input().split())
    train = [[0 for i in range(N)] for j in range(M)]
    for i in range(M):
        L,R = map(int,input().split())
        for j in range(L-1,R):
            train[i][j] = 1
    for i in range(Q):
        p,q = map(int,input().split())
        ans = 0
        for j in range(p-1,q):
            for k in range(M):
                if train[k][j] == 1:
                    ans += 1
        print(ans)
