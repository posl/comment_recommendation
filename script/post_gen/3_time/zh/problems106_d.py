Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n,m,q = map(int,raw_input().split())
    trains = []
    for i in xrange(m):
        trains.append(map(int,raw_input().split()))
    queries = []
    for i in xrange(q):
        queries.append(map(int,raw_input().split()))
    return n,m,q,trains,queries

=======
Suggestion 2

def main():
    nmq = input().split(" ")
    n = int(nmq[0])
    m = int(nmq[1])
    q = int(nmq[2])
    lr = []
    pq = []
    for i in range(m):
        lr.append(input().split(" "))
    for i in range(q):
        pq.append(input().split(" "))
    for i in range(q):
        count = 0
        for j in range(m):
            if int(pq[i][0]) <= int(lr[j][0]) and int(lr[j][1]) <= int(pq[i][1]):
                count += 1
        print(count)

=======
Suggestion 3

def main():
    N,M,Q = map(int,input().split())
    #print(N,M,Q)
    #print(type(N),type(M),type(Q))
    #L = [0]*M
    #R = [0]*M
    #P = [0]*Q
    #Q = [0]*Q
    #for i in range(M):
    #    L[i],R[i] = map(int,input().split())
    #for i in range(Q):
    #    P[i],Q[i] = map(int,input().split())
    #print(L,R,P,Q)
    #print(type(L),type(R),type(P),type(Q))
    L = []
    R = []
    P = []
    Q = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    for i in range(Q):
        p,q = map(int,input().split())
        P.append(p)
        Q.append(q)
    #print(L,R,P,Q)
    #print(type(L),type(R),type(P),type(Q))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[0]),type(R[0]),type(P[0]),type(Q[0]))
    #print(len(L),len(R),len(P),len(Q))
    #print(L[0],R[0],P[0],Q[0])
    #print(type(L[

=======
Suggestion 4

def fun():
    n,m,q = map(int, input().split())
    L = []
    R = []
    for i in range(m):
        l,r = map(int, input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(q):
        p,q = map(int, input().split())
        P.append(p)
        Q.append(q)
    for i in range(q):
        count = 0
        for j in range(m):
            if P[i] <= L[j] and R[j] <= Q[i]:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    N,M,Q = map(int, input().split())
    train = []
    for i in range(M):
        L,R = map(int, input().split())
        train.append([L,R])
    for i in range(Q):
        p,q = map(int, input().split())
        count = 0
        for j in range(M):
            if train[j][0] >= p and train[j][1] <= q:
                count += 1
        print(count)

=======
Suggestion 6

def binary_search(array, key):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

=======
Suggestion 7

def get_ints():
    return [int(x) for x in input().split()]

=======
Suggestion 8

def main():
    n,m,q = map(int,input().split())
    lr = [tuple(map(int,input().split())) for _ in range(m)]
    pq = [tuple(map(int,input().split())) for _ in range(q)]
    ans = [0 for _ in range(q)]
    for i in range(q):
        for j in range(m):
            if pq[i][0] <= lr[j][0] and lr[j][1] <= pq[i][1]:
                ans[i] += 1
    for i in range(q):
        print(ans[i])

main()

=======
Suggestion 9

def count_trains(l,r,train):
    count = 0
    for i in range(len(train)):
        if train[i][0] >= l and train[i][1] <= r:
            count += 1
    return count

=======
Suggestion 10

def main():
    # 读入数据
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        L, R = map(int, input().split())
        trains.append((L, R))
    queries = []
    for i in range(Q):
        p, q = map(int, input().split())
        queries.append((p, q))

    # 计算答案
    answers = []
    for p, q in queries:
        count = 0
        for L, R in trains:
            if p <= L and R <= q:
                count += 1
        answers.append(count)

    # 输出答案
    for ans in answers:
        print(ans)
