Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n, m, q = map(int, input().split())
    l = [0]*m
    r = [0]*m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    p = [0]*q
    q = [0]*q
    for i in range(q):
        p[i], q[i] = map(int, input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i] <= l[j] and r[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 3

def solve():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    # 为了方便起见，我们将L和R的元素都减1。
    for i in range(M):
        L[i] -= 1
        R[i] -= 1
    # 用二维数组C来记录答案。
    C = [[0] * N for i in range(N)]
    for i in range(M):
        for j in range(L[i], R[i] + 1):
            C[j][R[i]] += 1
    for i in range(N):
        for j in range(N - 1):
            C[i][j + 1] += C[i][j]
    for i in range(Q):
        print(C[p[i] - 1][q[i] - 1])

solve()

=======
Suggestion 4

def get_input():
    input_str = input("请输入N M Q：")
    input_list = input_str.split(" ")
    N = int(input_list[0])
    M = int(input_list[1])
    Q = int(input_list[2])
    print("N M Q = ",N,M,Q)
    L = []
    R = []
    for i in range(M):
        input_str = input("请输入L R：")
        input_list = input_str.split(" ")
        L.append(int(input_list[0]))
        R.append(int(input_list[1]))
    p = []
    q = []
    for i in range(Q):
        input_str = input("请输入p q：")
        input_list = input_str.split(" ")
        p.append(int(input_list[0]))
        q.append(int(input_list[1]))
    return N,M,Q,L,R,p,q

=======
Suggestion 5

def train_num(train, start, end):
    num = 0
    for i in range(len(train)):
        if train[i][0] >= start and train[i][1] <= end:
            num += 1
    return num

=======
Suggestion 6

def solve():
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
    for i in range(Q):
        count = 0
        for j in range(M):
            if P[i] <= L[j] and R[j] <= Q[i]:
                count += 1
        print(count)

=======
Suggestion 7

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
            if train[j][0] >= query[i][0] and train[j][1] <= query[i][1]:
                count += 1
        print(count)

main()

=======
Suggestion 8

def get_train_num(p,q):
    train_num = 0
    for i in range(1,M+1):
        if L[i] >= p and R[i] <= q:
            train_num += 1
    return train_num

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

    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug1")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug2")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug3")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug4")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug5")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug6")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug7")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug8")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug9")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug10")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug11")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug12")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug13")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug14")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("debug15")
    # print(n,m,q)
    # print(l,r)
    # print(p,q)

    # print("

=======
Suggestion 10

def main():
    n,m,q = map(int,input().split())
    L = [0] * m
    R = [0] * m
    p = [0] * q
    q = [0] * q
    for i in range(m):
        L[i],R[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i] <= L[j] and R[j] <= q[i]:
                count += 1
        print(count)
