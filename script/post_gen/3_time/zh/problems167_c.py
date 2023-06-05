Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
        a.append(c[i][1:])
        c[i].remove(c[i][1:])
    print(c)
    print(a)

=======
Suggestion 2

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    ans = 10**10
    for i in range(1 << N):
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
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 100000000
    for i in range(2 ** N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(understand[k] >= X for k in range(M)):
            min_cost = min(min_cost, cost)
    if min_cost == 100000000:
        print(-1)
    else:
        print(min_cost)

main()

=======
Suggestion 4

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    print(c)
    for i in range(n):
        a.append(c[i][1:])
    print(a)
    min_cost = 99999999999999
    for i in range(2**n):
        cost = 0
        level = [0 for _ in range(m)]
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j][0]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x and cost < min_cost:
            min_cost = cost
    if min_cost == 99999999999999:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(n,m,x)
    print(c)
    print(a)
    for i in range(n):
        for j in range(m):
            if a[i][j] < x:
                a[i][j] = 0
    print(a)
    for i in range(n):
        if sum(a[i]) == 0:
            print("-1")
            break
    else:
        print(sum(c[i][0] for i in range(n)))

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    books = []
    for i in range(N):
        books.append(list(map(int, input().split())))
    min_cost = 1000000
    for i in range(2**N):
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += books[j][0]
                for k in range(M):
                    understand[k] += books[j][k+1]
        if min(understand) >= X and cost < min_cost:
            min_cost = cost
    if min_cost == 1000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 7

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**5 * 12 + 1
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i >> j & 1:
                cost += C[j]
                understanding = [understanding[k] + A[j][k] for k in range(M)]
        if all(understanding[k] >= X for k in range(M)):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost != 10**5 * 12 + 1 else -1)

solve()

=======
Suggestion 8

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = float("inf")
    for i in range(2**N):
        cost = 0
        understand = [0 for _ in range(M)]
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(understand[k] >= X for k in range(M)):
            ans = min(ans, cost)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

solve()

=======
Suggestion 9

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    min_cost = 100000000
    for i in range(2**n):
        cost = 0
        understanding = [0 for j in range(m)]
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    understanding[k] += a[j][k]
        if min(understanding) >= x:
            min_cost = min(min_cost, cost)
    if min_cost == 100000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 10

def get_min_cost(N, M, X, C, A):
    min_cost = -1
    for i in range(1, 1<<N):
        cost = 0
        understand = [0 for _ in range(M)]
        for j in range(N):
            if (i>>j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    return min_cost
