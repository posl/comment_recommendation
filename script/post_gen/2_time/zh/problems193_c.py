Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10 ** 9 + 1
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
    if ans == 10 ** 9 + 1:
        print(-1)
    else:
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
    min_price = 10000000000
    for i in range(N):
        if X[i] > 0:
            if P[i] < min_price:
                min_price = P[i]
    if min_price == 10000000000:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 3

def main():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))

    min_price = -1
    for shop in shops:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            else:
                min_price = min(min_price, shop[1])
    print(min_price)

=======
Suggestion 4

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
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            elif P[i] < min_price:
                min_price = P[i]
    print(min_price)

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
    min_price = -1
    for i in range(N):
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)

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

    minCost = 1000000000
    for i in range(N):
        if X[i] > 0:
            minCost = min(minCost, P[i])

    if minCost == 1000000000:
        print(-1)
    else:
        print(minCost)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_p = 10**9
    for i in range(n):
        if x[i] > 0:
            if p[i] < min_p:
                min_p = p[i]
    if min_p == 10**9:
        min_p = -1
    print(min_p)

=======
Suggestion 8

def get_min_money(n, shop_list):
    min_money = -1
    for i in range(n):
        if shop_list[i][2] > 0:
            if min_money == -1 or min_money > shop_list[i][1]:
                min_money = shop_list[i][1]
    return min_money

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_price = 10**9 + 1
    for i in range(n):
        if x[i] > 0:
            if p[i] < min_price:
                min_price = p[i]
    if min_price == 10**9 + 1:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def solve():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)

    ans = 10**9 + 1
    flag = False
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
            flag = True

    if flag:
        print(ans)
    else:
        print(-1)

solve()
