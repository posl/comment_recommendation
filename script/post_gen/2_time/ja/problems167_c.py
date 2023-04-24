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

    min_price = float("inf")
    for i in range(2**N):
        price = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1 == 1:
                price += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            min_price = min(min_price, price)
    if min_price == float("inf"):
        print(-1)
    else:
        print(min_price)

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
    ans = 10**9
    for i in range(2**N):
        cost = 0
        skill = [0]*M
        for j in range(N):
            if i>>j & 1:
                cost += C[j]
                for k in range(M):
                    skill[k] += A[j][k]
        if all(skill[k] >= X for k in range(M)):
            ans = min(ans, cost)
    print(-1 if ans == 10**9 else ans)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    ans = 10**10
    for i in range(2**N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(N, M, X)
    #print(C)
    #print(A)

    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1 == 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        #print(i, cost, understanding)
        if min(understanding) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
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

    min_cost = float("inf")
    for i in range(2**N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if i >> j & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(understand[k] >= X for k in range(M)):
            min_cost = min(min_cost, cost)

    if min_cost == float("inf"):
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += C[j]
        if sum >= ans:
            continue
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = sum
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    min_cost = float('inf')
    for i in range(2 ** N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                understanding = [u + a for u, a in zip(understanding, A[j])]
        if all(u >= X for u in understanding):
            min_cost = min(min_cost, cost)

    print(min_cost if min_cost != float('inf') else -1)

=======
Suggestion 8

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    #print(c)
    #print(a)
    min_cost = 1000000000
    for i in range(2**n):
        total_cost = 0
        total_a = [0]*m
        for j in range(n):
            if ((i>>j) & 1):
                total_cost += c[j]
                for k in range(m):
                    total_a[k] += a[j][k]
        flag = True
        for k in range(m):
            if total_a[k] < x:
                flag = False
                break
        if flag:
            min_cost = min(min_cost,total_cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 9

def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)

    ans = 10**9
    for i in range(2**N):
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(X <= u for u in understand):
            ans = min(ans,cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def main():
    n,m,x = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 10**9
    for i in range(2**n):
        cost = 0
        u = [0]*m
        for j in range(n):
            if i & (1<<j):
                cost += a[j][0]
                for k in range(m):
                    u[k] += a[j][k+1]
        if min(u) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

main()
