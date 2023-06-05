Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = -1
    for i in range(2 ** N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                understanding = [understanding[k] + A[j][k] for k in range(M)]
        if all(understanding[k] >= X for k in range(M)):
            if min_cost < 0:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 2

def max_num(list1):
    list1.sort()
    return list1[-1]

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                understanding = [understanding[k]+A[j][k] for k in range(M)]
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 4

def get_min_cost(n, m, x, c, a):
    min_cost = -1
    for i in range(1, 1 << n):
        cost = 0
        u = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if all(x <= ui for ui in u):
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    return min_cost

=======
Suggestion 5

def main():
    line1 = input().split()
    line2 = input().split()
    line3 = input().split()
    line4 = input().split()
    line5 = input().split()
    line6 = input().split()
    line7 = input().split()
    line8 = input().split()
    line9 = input().split()
    line10 = input().split()
    line11 = input().split()
    line12 = input().split()
    line13 = input().split()
    line14 = input().split()
    line15 = input().split()
    line16 = input().split()
    line17 = input().split()
    line18 = input().split()
    line19 = input().split()
    line20 = input().split()
    line21 = input().split()
    line22 = input().split()
    line23 = input().split()
    line24 = input().split()
    line25 = input().split()
    line26 = input().split()
    line27 = input().split()
    line28 = input().split()
    line29 = input().split()
    line30 = input().split()
    line31 = input().split()
    line32 = input().split()
    line33 = input().split()
    line34 = input().split()
    line35 = input().split()
    line36 = input().split()
    line37 = input().split()
    line38 = input().split()
    line39 = input().split()
    line40 = input().split()
    line41 = input().split()
    line42 = input().split()
    line43 = input().split()
    line44 = input().split()
    line45 = input().split()
    line46 = input().split()
    line47 = input().split()
    line48 = input().split()
    line49 = input().split()
    line50 = input().split()
    line51 = input().split()
    line52 = input().split()
    line53 = input().split()
    line54 = input().split()
    line55 = input().split()
    line56 = input().split()
    line57 = input().split()
    line58 = input().split()
    line59 = input().split()
    line60 = input().split()
    line61 = input().split()
    line62 = input().split()
    line

=======
Suggestion 6

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)
    for i in range(n):
        for j in range(m):
            a[i][j] += c[i][0]
    print(a)
    # for i in range(n):
    #     for j in range(m):
    #         print(a[i][j])
    ans = 100000000
    for i in range(2**n):
        cost = 0
        level = [0]*m
        for j in range(n):
            if (i>>j)&1:
                cost += c[j][0]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans,cost)
    if ans == 100000000:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    # 读取数据
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    # 穷举
    min_cost = float('inf')
    for i in range(2 ** N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(x >= X for x in understand):
            min_cost = min(min_cost, cost)
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 8

def solve():
    N,M,X=map(int,input().split())
    l=[]
    for i in range(N):
        l.append(list(map(int,input().split())))
    #print(l)
    cost=0
    min_cost=-1
    for i in range(2**N):
        cost=0
        level=[0]*M
        for j in range(N):
            if ((i>>j)&1):
                cost+=l[j][0]
                for k in range(M):
                    level[k]+=l[j][k+1]
        #print(cost,level)
        if min(level)>=X:
            if min_cost==-1:
                min_cost=cost
            elif min_cost>cost:
                min_cost=cost
    print(min_cost)
solve()

=======
Suggestion 9

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    print(c)
    print(a)
    #print(n,m,x)
    #print(c)
    #print(a)
    #print(a[0])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[9][2])
    #print(a[10][0])
    #print(a[10][1])
    #print(a[10][2])
    #print(a[11][0])
    #print(a[11][1])
    #print(a[11][2])
    #print(a[12][0])
    #print(a[12][1])
    #print(a[12][2])
    #print(a[13][0])
    #print(a[13][1])
    #print(a[13][2])
    #print(a[14][0])
    #print(a[14][1])
    #print(a

=======
Suggestion 10

def get_num():
    N,M,X = map(int,input().split())
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    # print(N,M,X)
    # print(type(N),type(M),type(X))
    # print(type(N))
    # print(type(M))
    # print(type(X))
    # print(type(N),type(M),type(X))
    return N,M,X
