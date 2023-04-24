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
    min_cost = 10**6
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i>>j & 1:
                cost += C[j]
                understanding = [x+y for x,y in zip(understanding, A[j])]
        if all(x >= X for x in understanding):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost != 10**6 else -1)

=======
Suggestion 2

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**8
    for i in range(2**N):
        cost = 0
        U = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    U[k] += A[j][k]
        if all(u>=X for u in U):
            ans = min(ans, cost)
    if ans == 10**8:
        print(-1)
    else:
        print(ans)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        C.append(list(map(int, input().split())))
        A.append(C[i][1:])
        del C[i][1:]
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j][0]
                for k in range(M):
                    understanding[k] += A[j][k]
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    #print(c)
    #print(a)
    min_cost = 1000000000
    for i in range(2**n):
        cost = 0
        u = [0]*m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if min(u) >= x:
            min_cost = min(min_cost, cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    #print(n, m, x)
    #print(c)
    #print(a)
    #print('----')
    cost = 10**9
    for i in range(2**n):
        #print('i:', i)
        tmp = [0 for _ in range(m)]
        tmp_cost = 0
        for j in range(n):
            if ((i >> j) & 1):
                tmp_cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        #print(tmp)
        #print(tmp_cost)
        #print('----')
        flag = True
        for j in range(m):
            if tmp[j] < x:
                flag = False
        if flag:
            cost = min(cost, tmp_cost)
    if cost == 10**9:
        print(-1)
    else:
        print(cost)

=======
Suggestion 6

def main():
    # input
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    
    # compute
    ans = -1
    for i in range(2 ** n):
        understanding = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                cost += c[j]
                understanding = [understanding[k] + a[j][k] for k in range(m)]
        if min(understanding) >= x:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    
    # output
    print(ans)

=======
Suggestion 7

def main():
    n, m, x = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    min_cost = -1
    for i in range(1<<n):
        cost = 0
        understand = [0]*m
        for j in range(n):
            if (i>>j)&1:
                cost += a[j][0]
                for k in range(m):
                    understand[k] += a[j][k+1]
        if min(understand) >= x:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 8

def get_input():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    return n, m, x, c, a

=======
Suggestion 9

def read_data():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(0)
        a.append([])
        c[i], *a[i] = map(int, input().split())
    return n, m, x, c, a

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
