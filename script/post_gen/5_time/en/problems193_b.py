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
    min_price = 1000000001
    for i in range(N):
        if X[i] > 0:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == 1000000001:
        min_price = -1
    print(min_price)

=======
Suggestion 2

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
            min_price = min(min_price, P[i])
    if min_price == 10**9:
        print(-1)
    else:
        print(min_price)

main()

=======
Suggestion 3

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
    ans = 10**10
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min_price = -1
    for i in range(n):
        if x[i] > 0:
            if min_price == -1:
                min_price = p[i]
            else:
                min_price = min(min_price, p[i])
    print(min_price)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min = 10**9
    for i in range(n):
        if x[i] > a[i]:
            if min > p[i]:
                min = p[i]
    if min == 10**9:
        print(-1)
    else:
        print(min)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        A_i, P_i, X_i = input().split()
        A.append(int(A_i))
        P.append(int(P_i))
        X.append(int(X_i))
    min_price = -1
    for i in range(N):
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)

=======
Suggestion 7

def buy_play_snuke(N, A, P, X):
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1:
                result = P[i]
            else:
                result = min(result, P[i])
    return result

=======
Suggestion 8

def solve():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    min_price = 10**9 + 1
    for i in range(N):
        A, P, X = shops[i]
        if X > 0:
            min_price = min(min_price, P)
    if min_price == 10**9 + 1:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 9

def solve():
    N = int(input())
    shops = [list(map(int, input().split())) for _ in range(N)]
    min_price = float('inf')
    for shop in shops:
        if shop[2] > shop[0]:
            min_price = min(min_price, shop[1])
    if min_price == float('inf'):
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def main():
    n = int(input())
    shops = []
    for i in range(0, n):
        shops.append([int(x) for x in input().split()])
    min = -1
    for i in range(0, n):
        if shops[i][2] > 0:
            if min == -1 or shops[i][1] < min:
                min = shops[i][1]
    print(min)
