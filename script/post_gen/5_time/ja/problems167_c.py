Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_, *a_ = map(int, input().split())
        c.append(c_)
        a.append(a_)
    ans = float('inf')
    for i in range(1 << n):
        cost = 0
        u = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if all(v >= x for v in u):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 2

def main():
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    #print(c)
    #print(a)
    min_cost = 1000000000
    for i in range(2**n):
        cost = 0
        understand = [0]*m
        for j in range(n):
            if (i>>j)&1:
                cost += c[j]
                for k in range(m):
                    understand[k] += a[j][k]
        #print(understand)
        if min(understand) >= x:
            min_cost = min(min_cost, cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 3

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**9
    for i in range(1 << n):
        tmp = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        if min(tmp) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    n,m,x=map(int,input().split())
    c=[]
    a=[]
    for i in range(n):
        tmp=list(map(int,input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    #print(c)
    #print(a)
    min_cost=1000000
    for i in range(2**n):
        #print(i)
        cost=0
        understanding=[0]*m
        for j in range(n):
            if ((i>>j)&1):
                cost+=c[j]
                for k in range(m):
                    understanding[k]+=a[j][k]
        #print(understanding)
        if (min(understanding)>=x):
            min_cost=min(min_cost,cost)
    if (min_cost==1000000):
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    N, M, X = map(int, input().split())

    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    min_cost = 10**10
    for i in range(1<<N):
        cost = 0
        skill = [0] * M
        for j in range(N):
            if i & (1<<j):
                cost += C[j]
                for k in range(M):
                    skill[k] += A[j][k]
        if min(skill) >= X:
            min_cost = min(min_cost, cost)

    if min_cost == 10**10:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 6

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for _ in range(n):
        c_i, *a_i = map(int, input().split())
        c.append(c_i)
        a.append(a_i)
    ans = float('inf')
    for i in range(2**n):
        tmp = [0]*m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                for k in range(m):
                    tmp[k] += a[j][k]
                cost += c[j]
        if all([tmp_i >= x for tmp_i in tmp]):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    print(c)
    print(a)
    print(n,m,x)

=======
Suggestion 8

def check(books, n, m, x, c, a):
  #print("n,m,x,c,a", n,m,x,c,a)
  #print("books", books)
  #print("c", c)
  #print("a", a)
  #print("n", n)
  #print("m", m)
  #print("x", x)
  sum = 0
  for i in range(n):
    sum = sum + books[i] * c[i]
    #print("sum", sum)
  if sum >= x:
    return True
  else:
    return False

=======
Suggestion 9

def main():
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**9
    for i in range(2**n):
        tmp = [0]*m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        if min(tmp) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**10
    for i in range(2**n):
        tmp = [0]*m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                for k in range(m):
                    tmp[k] += a[j][k]
                cost += c[j]
        if min(tmp) >= x:
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
