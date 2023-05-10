Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [0] * n
    p = [0] * n
    x = [0] * n
    for i in range(n):
        a[i], p[i], x[i] = map(int, input().split())

    ans = 10**9
    for i in range(n):
        if x[i] - a[i] > 0:
            ans = min(ans, p[i])

    print(ans if ans != 10**9 else -1)

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 10 ** 9 + 1
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    #print(A, P, X)
    min_price = 10000000000
    for i in range(N):
        if X[i] > A[i]:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == 10000000000:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 4

def solve():
    n = int(input())
    min_cost = 10**9 + 1
    for _ in range(n):
        a, p, x = map(int, input().split())
        if x > a:
            min_cost = min(min_cost, p)
    if min_cost == 10**9 + 1:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 1000000000
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 1000000000:
        ans = -1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10 ** 9 + 7
    for i in range(N):
        if X[i] - A[i] > 0:
            ans = min(ans, P[i])
    if ans == 10 ** 9 + 7:
        ans = -1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    ans = -1
    for i in range(n):
        if x[i] > 0:
            if ans == -1:
                ans = p[i]
            else:
                ans = min(ans, p[i])
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    shops = []
    for _ in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    ans = 10**9 + 1
    for a, p, x in shops:
        if x >= 1:
            ans = min(ans, p)
    if ans == 10**9 + 1:
        ans = -1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A, P, X = [], [], []
    for _ in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = float("inf")
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])
    if min_price == float("inf"):
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)

    min_price = 10000000000
    for i in range(N):
        if X[i] > A[i]:
            if min_price > P[i]:
                min_price = P[i]

    if min_price == 10000000000:
        print(-1)
    else:
        print(min_price)
