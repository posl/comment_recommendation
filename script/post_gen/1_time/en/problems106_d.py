Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    P, Q = zip(*PQ)
    P, Q = map(lambda x: [0] + list(x), [P, Q])

    # cumulative sum
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for L, R in LR:
        C[L][R] += 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            C[i][j] += C[i][j - 1]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            C[i][j] += C[i - 1][j]

    # query
    for i in range(1, Q + 1):
        print(C[Q[i]][Q[i]] - C[P[i] - 1][Q[i]] - C[Q[i]][P[i] - 1] + C[P[i] - 1][P[i] - 1])

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(trains)
    #print(queries)
    #print(N, M, Q)
    for p, q in queries:
        print(sum([1 for l, r in trains if l >= p and r <= q]))

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    p = []
    q = []
    for i in range(Q):
        p_, q_ = map(int, input().split())
        p.append(p_)
        q.append(q_)
    #print(N, M, Q)
    #print(L)
    #print(R)
    #print(p)
    #print(q)
    for i in range(Q):
        count = 0
        for j in range(M):
            if L[j] >= p[i] and R[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 4

def main():
    # input
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    ans = [0] * Q
    for i in range(Q):
        for j in range(M):
            if LR[j][0] <= PQ[i][0] and PQ[i][1] <= LR[j][1]:
                ans[i] += 1

    # output
    for i in range(Q):
        print(ans[i])

=======
Suggestion 5

def main():
    n, m, q = map(int, input().split())
    trains = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        l, r = map(int, input().split())
        trains[l][r] += 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            trains[i][j] += trains[i][j - 1]
    for _ in range(q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += trains[i][q] - trains[i][p - 1]
        print(ans)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        train[L - 1] += 1
        train[R] -= 1
    for i in range(1, N + 1):
        train[i] = train[i - 1] + train[i]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])

=======
Suggestion 7

def get_input():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    p = []
    q = []
    for i in range(Q):
        pi, qi = map(int, input().split())
        p.append(pi)
        q.append(qi)
    return N, M, Q, L, R, p, q

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    train = [[0] * (N + 1) for i in range(N + 1)]
    for _ in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1
    for i in range(N + 1):
        for j in range(N):
            train[i][j + 1] += train[i][j]
    for _ in range(Q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += train[i][q] - train[i][p - 1]
        print(ans)

=======
Suggestion 9

def main():
    #read input
    n, m, q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]

    #process
    #sum[i][j] = number of trains that runs strictly within the section from City i to City j
    sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for train in trains:
        sum[train[0]][train[1]] += 1

    #cumulative sum
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum[i][j] += sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

    #output
    for query in queries:
        print(sum[query[1]][query[1]] - sum[query[0]-1][query[1]] - sum[query[1]][query[0]-1] + sum[query[0]-1][query[0]-1])

main()

=======
Suggestion 10

def main():
    # read input
    n, m, q = map(int, input().split())
    train = [list(map(int, input().split())) for _ in range(m)]
    query = [list(map(int, input().split())) for _ in range(q)]

    # create array of 0s
    # array[i][j] = 0 if train j is not running between city i and i+1
    # array[i][j] = 1 if train j is running between city i and i+1
    array = [[0 for _ in range(m)] for _ in range(n)]

    # populate array
    for i in range(m):
        for j in range(train[i][0], train[i][1]):
            array[j-1][i] = 1

    # sum array for each query
    for i in range(q):
        print(sum(array[query[i][0]-1][query[i][1]-1]))

main()
