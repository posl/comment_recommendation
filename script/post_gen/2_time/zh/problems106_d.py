Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    #获取输入
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
Suggestion 2

def get_input():
    n, m, q = map(int, input().split())
    lr = []
    pq = []
    for i in range(m):
        lr.append(list(map(int, input().split())))
    for i in range(q):
        pq.append(list(map(int, input().split())))
    return n, m, q, lr, pq

=======
Suggestion 3

def get_input():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        L, R = map(int, input().split())
        trains.append((L, R))
    queries = []
    for i in range(Q):
        p, q = map(int, input().split())
        queries.append((p, q))
    return N, M, Q, trains, queries

=======
Suggestion 4

def get_num_of_train(start,end,train_list):
    num_of_train = 0
    for train in train_list:
        if train[0] >= start and train[1] <= end:
            num_of_train += 1
    return num_of_train

=======
Suggestion 5

def main():
    #读取输入
    N,M,Q = map(int,input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    p = [0]*Q
    q = [0]*Q
    for i in range(Q):
        p[i],q[i] = map(int,input().split())
    #计算答案
    #每个城市的列车数量
    trains = [0]*(N+1)
    for i in range(M):
        for j in range(L[i],R[i]+1):
            trains[j]+=1
    #每个城市的列车数量的前缀和
    trains_prefix = [0]*(N+1)
    trains_prefix[1] = trains[1]
    for i in range(2,N+1):
        trains_prefix[i] = trains_prefix[i-1]+trains[i]
    #每个查询的答案
    for i in range(Q):
        print(trains_prefix[q[i]]-trains_prefix[p[i]-1])

=======
Suggestion 6

def read_input():
    #input = sys.stdin.readline
    #N, M, Q = list(map(int, input().split()))
    #L = [0] * M
    #R = [0] * M
    #for i in range(M):
    #    L[i], R[i] = list(map(int, input().split()))
    #P = [0] * Q
    #Q = [0] * Q
    #for i in range(Q):
    #    P[i], Q[i] = list(map(int, input().split()))
    N, M, Q = 10, 10, 10
    L = [1, 2, 4, 4, 4, 5, 6, 6, 7, 10]
    R = [6, 9, 5, 7, 7, 8, 6, 7, 9, 10]
    P = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1]
    Q = [8, 9, 10, 8, 9, 10, 8, 9, 10, 10]
    return N, M, Q, L, R, P, Q

=======
Suggestion 7

def problem106_d():
    n,m,q = map(int,input().split())
    l = [0]*m
    r = [0]*m
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    p = [0]*q
    q = [0]*q
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i]<=l[j] and r[j]<=q[i]:
                count += 1
        print(count)
problem106_d()

=======
Suggestion 8

def main():
    n,m,q = map(int,input().split())
    train = []
    for i in range(m):
        train.append(list(map(int,input().split())))
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if query[i][0] <= train[j][0] and query[i][1] >= train[j][1]:
                count += 1
        print(count)

=======
Suggestion 9

def main():
    #读取输入
    N,M,Q = map(int,input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    P = [0]*Q
    Q = [0]*Q
    for i in range(Q):
        P[i],Q[i] = map(int,input().split())
    #处理输入
    #预处理
    pre = [0]*N
    for i in range(M):
        pre[L[i]-1] += 1
        if R[i] != N:
            pre[R[i]] -= 1
    for i in range(1,N):
        pre[i] += pre[i-1]
    #处理查询
    for i in range(Q):
        print(pre[Q[i]-1]-pre[P[i]-1])
    return 0

=======
Suggestion 10

def main():
    n, m, q = map(int, input().split())
    lr = []
    for i in range(m):
        lr.append(list(map(int, input().split())))
    pq = []
    for i in range(q):
        pq.append(list(map(int, input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if pq[i][0] <= lr[j][0] and lr[j][1] <= pq[i][1]:
                count += 1
        print(count)
