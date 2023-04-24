Synthesizing 10/10 solutions

=======
Suggestion 1

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
    min_price = 10**9
    for i in range(N):
        if X[i] > A[i]:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == 10**9:
        min_price = -1
    print(min_price)

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
    min_price = 1000000001
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])
    if min_price == 1000000001:
        return -1
    else:
        return min_price

print(solve())

=======
Suggestion 3

def main():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_p = 10**9
    for i in range(N):
        if X[i] > A[i] and min_p > P[i]:
            min_p = P[i]
    if min_p == 10**9:
        print(-1)
    else:
        print(min_p)

=======
Suggestion 4

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
    min_p = 10**9
    for i in range(n):
        if x[i] > a[i]:
            min_p = min(min_p, p[i])
    if min_p == 10**9:
        print(-1)
    else:
        print(min_p)

=======
Suggestion 5

def solve():
    n = int(input())
    a = [0] * n
    p = [0] * n
    x = [0] * n
    for i in range(n):
        a[i], p[i], x[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10**9:
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
        a, p, x = [int(i) for i in input().split()]
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = float('inf')
    for i in range(N):
        if X[i] > 0:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == float('inf'):
        min_price = -1
    print(min_price)

=======
Suggestion 7

def solve():
    N = int(input())
    shops = []
    for _ in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    shops.sort(key=lambda x: x[0])
    for A, P, X in shops:
        if X > A:
            return P
    return -1

print(solve())

=======
Suggestion 8

def main():
    N = int(input())
    shops = []
    for i in range(N):
        shops.append(list(map(int, input().split())))
    min_price = -1
    for i in range(N):
        if shops[i][2] > 0 and (min_price == -1 or min_price > shops[i][1]):
            min_price = shops[i][1]
    print(min_price)

=======
Suggestion 9

def main():
    N = int(input())
    shops = []
    for i in range(N):
        shops.append(list(map(int, input().split())))
    shops.sort(key=lambda x: x[0])
    for i in range(N):
        if shops[i][2] > shops[i][1]:
            print(shops[i][1])
            return
    print(-1)

=======
Suggestion 10

def buy_play_snuke(n, shops):
    min_price = -1
    for shop in shops:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            else:
                min_price = min(min_price, shop[1])
    return min_price
