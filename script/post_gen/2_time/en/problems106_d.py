Synthesizing 10/10 solutions

=======
Suggestion 1

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
        count = 0
        for j in range(M):
            if p[i] <= L[j] and R[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 2

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
        count = 0
        for j in range(M):
            if L[j] >= p[i] and R[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0]*Q
    q = [0]*Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        cnt = 0
        for j in range(M):
            if L[j] >= p[i] and R[j] <= q[i]:
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int, input().split())))
    PQ = []
    for i in range(Q):
        PQ.append(list(map(int, input().split())))
    LR = sorted(LR, key=lambda x: x[1])
    for p, q in PQ:
        count = 0
        for l, r in LR:
            if l >= p and r <= q:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    trains = [0] * (N + 1)
    for i in range(M):
        L, R = map(int, input().split())
        trains[L - 1] += 1
        trains[R] -= 1
    for i in range(1, N + 1):
        trains[i] += trains[i - 1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(trains[q] - trains[p - 1])

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    train = [[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            train[i][j] += train[i][j-1] + train[i-1][j] - train[i-1][j-1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q][q]-train[p-1][q]-train[q][p-1]+train[p-1][p-1])

=======
Suggestion 7

def main():
    # read input
    N, M, Q = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(M)]
    PQ = [tuple(map(int, input().split())) for _ in range(Q)]
    # create cumulative sum
    cumsum = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in LR:
        cumsum[l][r] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cumsum[i][j] += cumsum[i - 1][j] + cumsum[i][j - 1] - cumsum[i - 1][j - 1]
    # output
    for p, q in PQ:
        print(cumsum[q][q] - cumsum[p - 1][q] - cumsum[q][p - 1] + cumsum[p - 1][p - 1])

=======
Suggestion 8

def main():
    n, m, q = [int(x) for x in input().split()]
    trains = [0] * (n + 1)
    for i in range(m):
        l, r = [int(x) for x in input().split()]
        trains[l - 1] += 1
        trains[r] -= 1
    for i in range(n):
        trains[i + 1] += trains[i]
    for i in range(q):
        p, q = [int(x) for x in input().split()]
        print(trains[q] - trains[p - 1])

=======
Suggestion 9

def main():
    #read input
    n,m,q = map(int,input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int,input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int,input().split())))
    #solve problem
    for i in range(q):
        print(solve(trains,queries[i][0],queries[i][1]))

=======
Suggestion 10

def main():
    import sys
    #f = open('test.txt','r')
    f = sys.stdin
    n,m,q = map(int,f.readline().split())
    trains = [list(map(int,f.readline().split())) for i in range(m)]
    queries = [list(map(int,f.readline().split())) for i in range(q)]
    #print(n,m,q)
    #print(trains)
    #print(queries)
    for query in queries:
        count = 0
        for train in trains:
            if train[0] >= query[0] and train[1] <= query[1]:
                count += 1
        print(count)
