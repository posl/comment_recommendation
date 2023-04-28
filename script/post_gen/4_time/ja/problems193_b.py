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
    ans = -1
    for i in range(N):
        if X[i] > A[i]:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

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

    min_price = 1000000000
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])

    if min_price == 1000000000:
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
    min_price = -1
    for i in range(N):
        if X[i] > A[i]:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)
    return

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a,p,x = map(int,input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    cost = -1
    for i in range(N):
        if X[i] > 0:
            if cost == -1:
                cost = P[i]
            else:
                cost = min(cost,P[i])
    print(cost)

=======
Suggestion 5

def main():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    ans = 10**9+1
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10**9+1:
        ans = -1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        p.append(tmp[1])
        x.append(tmp[2])
    ans = 10**9
    for i in range(n):
        if x[i] - a[i] > 0:
            ans = min(ans, p[i])
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for _ in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)

    min_price = 10 ** 9
    for i in range(n):
        if x[i] > a[i]:
            min_price = min(min_price, p[i])
    if min_price == 10 ** 9:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 8

def calc_min_price(n, a_list, p_list, x_list):
    min_price = -1
    for i in range(n):
        if x_list[i] > 0:
            if min_price == -1:
                min_price = p_list[i]
            else:
                min_price = min(min_price, p_list[i])
    return min_price

=======
Suggestion 9

def main():
    n = int(input())
    stores = [list(map(int, input().split())) for _ in range(n)]
    min_price = 10 ** 9 + 1
    for store in stores:
        time = store[0]
        price = store[1]
        stock = store[2]
        if stock > 0:
            min_price = min(min_price, price)
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def calc_cost(a,p,x):
    if x == 0:
        return -1
    else:
        return p
