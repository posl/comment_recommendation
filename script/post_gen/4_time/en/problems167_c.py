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
    
    min_cost = float('inf')
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)

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

    min_cost = float('inf')
    for i in range(2 ** N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            min_cost = min(min_cost, cost)

    print(min_cost if min_cost != float('inf') else -1)

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
    ans = 9999999999999999
    for i in range(2**N):
        tmp = 0
        tmpA = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                tmp += C[j]
                for k in range(M):
                    tmpA[k] += A[j][k]
        if min(tmpA) >= X:
            ans = min(ans, tmp)
    if ans == 9999999999999999:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    min_cost = 10**5 * n + 1
    for i in range(2**n):
        cost = 0
        understanding = [0] * m
        for j in range(n):
            if ((i >> j) & 1):
                cost += c[j]
                for k in range(m):
                    understanding[k] += a[j][k]
        if all(x <= y for y in understanding):
            min_cost = min(min_cost, cost)
    if min_cost == 10**5 * n + 1:
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
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**9
    for i in range(2**n):
        tmp = 0
        tmpa = [0]*m
        for j in range(n):
            if (i>>j)&1:
                tmp += c[j]
                for k in range(m):
                    tmpa[k] += a[j][k]
        if min(tmpa)>=x:
            ans = min(ans, tmp)
    if ans==10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        Ci, Ai = map(int, input().split())
        C.append(Ci)
        A.append(Ai)

    min_cost = -1
    for i in range(2**N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)

    print(min_cost)

=======
Suggestion 7

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    cost = 0
    for i in range(2**n):
        bit = []
        for j in range(n):
            if ((i >> j) & 1):
                bit.append(1)
            else:
                bit.append(0)
        if sum(bit)==0:
            continue
        sum_a = [0 for i in range(m)]
        for j in range(n):
            if bit[j]==1:
                for k in range(m):
                    sum_a[k] += a[j][k]
        if min(sum_a)>=x:
            cost = min([cost,sum([c[j]*bit[j] for j in range(n)])])
    if cost==0:
        print(-1)
    else:
        print(cost)

=======
Suggestion 8

def main():
    N, M, X = map(int, input().split())
    books = []
    for i in range(N):
        books.append(list(map(int, input().split())))
    min_cost = -1
    for i in range(2**N):
        cost = 0
        algos = [0]*M
        for j in range(N):
            if i >> j & 1:
                cost += books[j][0]
                for k in range(M):
                    algos[k] += books[j][k+1]
        if min_cost == -1:
            if min(algos) >= X:
                min_cost = cost
        else:
            if min(algos) >= X:
                min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 9

def main():
    n,m,x = map(int,input().split())
    book = []
    for i in range(n):
        book.append(list(map(int,input().split())))
    ans = min([sum([book[i][0] for i in range(n) if j & (1 << i)]) for j in range(2**n) if sum([book[i][j+1] for i in range(n)]) >= x])
    print(ans if ans < 10**5 else -1)

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
