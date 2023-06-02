Synthesizing 10/10 solutions

=======
Suggestion 1

def find_train_num(citys, trains, querys):
    # citys: 城市数目
    # trains: 列车数目
    # querys: 查询数目
    # trains_list: 列车列表
    # querys_list: 查询列表
    trains_list = []
    querys_list = []
    for i in range(trains):
        trains_list.append(list(map(int, input().split())))
    for j in range(querys):
        querys_list.append(list(map(int, input().split())))
    for k in range(querys):
        count = 0
        for l in range(trains):
            if querys_list[k][0] <= trains_list[l][0] and trains_list[l][1] <= querys_list[k][1]:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    N,M,Q = map(int,input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int,input().split())))
    pq = []
    for i in range(Q):
        pq.append(list(map(int,input().split())))
    for i in range(Q):
        count = 0
        for j in range(M):
            if pq[i][0] <= LR[j][0] and LR[j][1] <= pq[i][1]:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    train = []
    for i in range(M):
        train.append(list(map(int, input().split())))
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        temp = 0
        for j in range(M):
            if query[i][0] <= train[j][0] <= train[j][1] <= query[i][1]:
                temp += 1
        print(temp)

=======
Suggestion 4

def main():
    # 读取输入
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    # 为列车的左端点和右端点分别建立累计和
    L = [0] * (N + 2)
    R = [0] * (N + 2)
    for l, r in LR:
        L[l] += 1
        R[r + 1] -= 1
    for i in range(1, N + 2):
        L[i] += L[i - 1]
        R[i] += R[i - 1]
    # 计算累计和的差，即为答案
    for p, q in PQ:
        print(L[q] - L[p - 1] - R[q])

=======
Suggestion 5

def main():
    n,m,q = map(int, input().split())
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
            if l[j] >= p[i] and r[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 6

def findNumOfTrain(N,M,Q,train,query):
    #train = [[1, 1], [1, 2], [2, 2]]
    #query = [[1, 2]]
    result = []
    for i in range(Q):
        numOfTrain = 0
        for j in range(M):
            if train[j][0] >= query[i][0] and train[j][1] <= query[i][1]:
                numOfTrain += 1
        result.append(numOfTrain)
    return result

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    P = [0] * Q
    Q = [0] * Q
    for i in range(Q):
        P[i], Q[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(M):
            if (L[j] >= P[i] and R[j] <= Q[i]):
                count += 1
        print(count)

=======
Suggestion 8

def main():
    # 读取输入
    line = input()
    n, m, q = [int(i) for i in line.split()]
    trains = []
    for i in range(m):
        line = input()
        l, r = [int(j) for j in line.split()]
        trains.append([l, r])
    queries = []
    for i in range(q):
        line = input()
        p, q = [int(j) for j in line.split()]
        queries.append([p, q])

    # 计算
    trains.sort(key=lambda x: x[0])
    trains.sort(key=lambda x: x[1])
    queries.sort(key=lambda x: x[0])
    queries.sort(key=lambda x: x[1])

    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        print(count)

=======
Suggestion 9

def get_input():
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
Suggestion 10

def main():
    n,m,q = map(int,input().split())
    l = [0 for i in range(m)]
    r = [0 for i in range(m)]
    p = [0 for i in range(q)]
    q = [0 for i in range(q)]
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i]<=l[j] and r[j]<=q[i]:
                count += 1
        print(count)
