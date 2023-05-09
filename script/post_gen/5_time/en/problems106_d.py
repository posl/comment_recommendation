Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    trains = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        L = LR[i][0] - 1
        R = LR[i][1] - 1
        for j in range(L, R + 1):
            trains[j][i] = 1
    trains = [[sum(row[:i]) for i in range(M + 1)] for row in trains]
    for i in range(Q):
        P = PQ[i][0] - 1
        Q = PQ[i][1] - 1
        print(sum([trains[j][Q] - trains[j][P] for j in range(P, Q + 1)]))

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    for p, q in PQ:
        print(sum(1 for l, r in LR if p <= l <= r <= q))

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    L, R = [], []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    P, Q = [], []
    for i in range(Q):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)
    ans = []
    for i in range(Q):
        ans.append(sum([1 for i in range(M) if P[i] <= L[i] and R[i] <= Q[i]]))
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    LR = []
    for _ in range(M):
        LR.append(list(map(int, input().split())))
    pq = []
    for _ in range(Q):
        pq.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[1])
    for p, q in pq:
        count = 0
        for l, r in LR:
            if p <= l and r <= q:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        trains.append(list(map(int, input().split())))
    trains.sort()
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(M):
            if trains[j][0] >= p and trains[j][1] <= q:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        trains.append(list(map(int, input().split())))
    trains.sort(key=lambda x: x[0])
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(M):
            if trains[j][0] < p:
                continue
            if trains[j][1] > q:
                break
            count += 1
        print(count)

=======
Suggestion 7

def get_input():
    n, m, q = map(int, input().split())
    l = [0] * m
    r = [0] * m
    p = [0] * q
    q = [0] * q
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    for i in range(q):
        p[i], q[i] = map(int, input().split())
    return n, m, q, l, r, p, q

=======
Suggestion 8

def count_trains_within_section(trains, p, q):
    count = 0
    for train in trains:
        if p <= train[0] and train[1] <= q:
            count += 1
    return count

=======
Suggestion 9

def find_trains (L, R, p, q):
    trains = 0
    for i in range(len(L)):
        if L[i] >= p and R[i] <= q:
            trains += 1
    return trains

=======
Suggestion 10

def get_input():
    return list(map(int, input().split()))
