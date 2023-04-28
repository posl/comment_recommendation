Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m,q=map(int,input().split())
    lr=[]
    for _ in range(m):
        l,r=map(int,input().split())
        lr.append((l,r))
    pq=[]
    for _ in range(q):
        p,q=map(int,input().split())
        pq.append((p,q))
    return n,m,q,lr,pq

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    LR.sort(key=lambda x: x[0])
    for pq in PQ:
        print(sum(1 for lr in LR if pq[0] <= lr[0] and lr[1] <= pq[1]))

=======
Suggestion 3

def main():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    lr.sort(key=lambda x: x[1])
    for i in range(q):
        p, q = pq[i]
        cnt = 0
        for j in range(m):
            if lr[j][0] >= p and lr[j][1] <= q:
                cnt += 1
        print(cnt)
    return

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        train = 0
        for j in range(M):
            if (p[i] <= L[j] and R[j] <= q[i]):
                train += 1
        print(train)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int, input().split())))
    PQ = []
    for i in range(Q):
        PQ.append(list(map(int, input().split())))
    for i in range(Q):
        count = 0
        for j in range(M):
            if LR[j][0] >= PQ[i][0] and LR[j][1] <= PQ[i][1]:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    n, m, q = map(int, input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))

    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        print(count)

=======
Suggestion 7

def get_input():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    return n, m, q, lr, pq

=======
Suggestion 8

def get_input():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for i in range(m)]
    pq = [list(map(int, input().split())) for i in range(q)]
    return n, m, q, lr, pq

=======
Suggestion 9

def main():
    n,m,q = map(int,input().split())
    train = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        l,r = map(int,input().split())
        train[i][l-1] += 1
        if r < n:
            train[i][r] -= 1
    for i in range(m):
        for j in range(n-1):
            train[i][j+1] += train[i][j]
    for i in range(m):
        for j in range(n-1):
            train[i][j+1] += train[i][j]
    for i in range(q):
        p,q = map(int,input().split())
        print(train[i][q-1]-train[i][p-2])

=======
Suggestion 10

def train_count(n, m, q, trains, queries):
    trains_count = []
    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        trains_count.append(count)
    return trains_count
