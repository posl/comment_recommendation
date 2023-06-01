Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m,q = map(int,input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int,input().split())))
    for i in range(q):
        p,q = map(int,input().split())
        count = 0
        for j in range(m):
            if trains[j][0] >= p and trains[j][1] <= q:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]

    # M列火车，火车i从城市L_i运行到城市R_i（有可能L_i=R_i）。
    # 国王高桥对以下Q事项感兴趣：
    # 在城市p_i到城市q_i这一段内严格运行的列车数量，也就是说，有多少列车j使p_i≦L_j，R_j≦q_i。
    # 虽然他是天才，但这一数据太多，他一个人无法处理。请为这些Q查询中的每一个找到答案，以帮助他。

    # 1 ≦ L_i ≦ R_i ≦ N (1 ≦ i ≦ M)
    # 1 ≦ p_i ≦ q_i ≦ N (1 ≦ i ≦ Q)

    # 1 2 3 4 5 6 7 8 9 10
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1

    # 1 2 3 4 5 6 7

=======
Suggestion 4

def get_input():
    n, m, q = map(int, raw_input().split())
    l = []
    r = []
    p = []
    q1 = []
    for i in range(m):
        l1, r1 = map(int, raw_input().split())
        l.append(l1)
        r.append(r1)
    for i in range(q):
        p1, q2 = map(int, raw_input().split())
        p.append(p1)
        q1.append(q2)
    return n, m, q, l, r, p, q1

=======
Suggestion 5

def main():
    n, m, q = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    p = []
    q = []
    for i in range(q):
        p_, q_ = map(int, input().split())
        p.append(p_)
        q.append(q_)
    for i in range(q):
        count = 0
        for j in range(m):
            if l[j] >= p[i] and r[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    N,M,Q = map(int,input().split())
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    for i in range(M):
        a,b = map(int,input().split())
        l[a] += 1
        r[b] += 1
    for i in range(1,N+1):
        l[i] += l[i-1]
        r[i] += r[i-1]
    for i in range(Q):
        p,q = map(int,input().split())
        print(r[q] - l[p-1])

=======
Suggestion 7

def read_input():
    n,m,q = [int(x) for x in input().split()]
    l = []
    r = []
    for i in range(m):
        l_i,r_i = [int(x) for x in input().split()]
        l.append(l_i)
        r.append(r_i)
    p = []
    q = []
    for i in range(q):
        p_i,q_i = [int(x) for x in input().split()]
        p.append(p_i)
        q.append(q_i)
    return n,m,q,l,r,p,q

=======
Suggestion 8

def run():
    n,m,q = map(int,input().split())
    l_r = []
    for _ in range(m):
        l_r.append(list(map(int,input().split())))
    p_q = []
    for _ in range(q):
        p_q.append(list(map(int,input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if l_r[j][0] >= p_q[i][0] and l_r[j][1] <= p_q[i][1]:
                count += 1
        print(count)
