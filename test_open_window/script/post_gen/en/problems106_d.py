Synthesizing 10/10 solutions

=======

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
    ans = [0] * Q
    for i in range(Q):
        for j in range(M):
            if L[j] <= p[i] and q[i] <= R[j]:
                ans[i] += 1
    for i in range(Q):
        print(ans[i])

main()

=======

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
        ans = 0
        for j in range(M):
            if p[i] <= L[j] and R[j] <= q[i]:
                ans += 1
        print(ans)

main()

=======

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
        print(sum([1 for j in range(M) if L[j] >= p[i] and R[j] <= q[i]]))

main()

=======

def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for query in queries:
        print(len([train for train in trains if query[0] <= train[0] and train[1] <= query[1]]))

=======

def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # print(trains)
    # print(queries)
    for p, q in queries:
        count = 0
        for train in trains:
            if train[0] < p and q < train[1]:
                count += 1
        print(count)

=======

def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for i in range(M)]
    queries = [list(map(int, input().split())) for i in range(Q)]

    for p, q in queries:
        ans = 0
        for L, R in trains:
            if L <= p and q <= R:
                ans += 1
        print(ans)

main()

=======

def main():
    import sys
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    # 0-indexed
    LR = [[l-1, r-1] for l, r in LR]
    PQ = [[p-1, q-1] for p, q in PQ]
    #print(LR)
    #print(PQ)
    #print()

=======

def main():
    n,m,q = map(int,input().split())
    lr = [list(map(int,input().split())) for _ in range(m)]
    pq = [list(map(int,input().split())) for _ in range(q)]
    ans = [0] * q
    for i in range(q):
        for j in range(m):
            if lr[j][0] >= pq[i][0] and lr[j][1] <= pq[i][1]:
                ans[i] += 1
    for i in range(q):
        print(ans[i])

=======

def main():
    #read input
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())

    #create a 2D array
    arr = [[0 for i in range(N)] for j in range(N)]

    #fill in the array
    for i in range(M):
        arr[L[i]-1][R[i]-1] += 1

    #calculate the prefix sum
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                arr[i][j] += arr[i][j-1]
            elif j == 0:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

    #calculate the answer
    for i in range(Q):
        if p[i] == 1 and q[i] == 1:
            print(arr[q[i]-1][q[i]-1])
        elif p[i] == 1:
            print(arr[q[i]-1][q[i]-1] - arr[q[i]-1][p[i]-2])
        elif q[i] == 1:
            print(arr[q[i]-1][q[i]-1] - arr[p[i]-2][q[i]-1])
        else:
            print(arr[q[i]-1][q[i]-1] - arr[q[i]-1][p[i]-2] - arr[p[i]-2][q[i]-1] + arr[p[i]-2][p[i]-2])

=======

def main():
    # Read input
    n,m,q = map(int,input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int,input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int,input().split())))
    
    # Count number of trains in each city
    train_count = [0] * (n+1)
    for train in trains:
        train_count[train[0]] += 1
        train_count[train[1]+1] -= 1
    
    # Calculate number of trains in each section
    for i in range(1,n+1):
        train_count[i] += train_count[i-1]
    
    # Count number of trains in each section
    section_count = [0] * (n+1)
    for i in range(1,n+1):
        section_count[i] = section_count[i-1] + train_count[i]
    
    # Answer queries
    for query in queries:
        print(section_count[query[1]] - section_count[query[0]-1])
