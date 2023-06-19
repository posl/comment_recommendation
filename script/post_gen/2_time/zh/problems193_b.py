Synthesizing 10/10 solutions

=======
Suggestion 1

def buy_game():
    n = int(input())

=======
Suggestion 2

def solve():
    N = int(input())
    stores = []
    for i in range(N):
        A, P, X = map(int, input().split())
        stores.append((A, P, X))

    min_cost = -1
    for i in range(N):
        A, P, X = stores[i]
        if X > 0:
            if min_cost == -1 or min_cost > P:
                min_cost = P

    print(min_cost)

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
    min_p = 10 ** 9 + 1
    for i in range(N):
        if X[i] > 0 and P[i] < min_p:
            min_p = P[i]
    if min_p == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_p)

=======
Suggestion 4

def get_min_money(N, shops):
    min_money = -1
    for i in range(N):
        if shops[i][2] > 0:
            if min_money == -1:
                min_money = shops[i][1]
            else:
                if shops[i][1] < min_money:
                    min_money = shops[i][1]
    return min_money

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
    result = -1
    for i in range(n):
        if x[i] > 0:
            if result == -1:
                result = p[i]
            else:
                result = min(result, p[i])
    print(result)

=======
Suggestion 6

def get_input():
    n = int(input())
    a_list = []
    p_list = []
    x_list = []
    for i in range(n):
        a, p, x = map(int, input().split())
        a_list.append(a)
        p_list.append(p)
        x_list.append(x)
    return n, a_list, p_list, x_list

=======
Suggestion 7

def solve():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min_price = 10**9
    for i in range(n):
        if x[i] > 0:
            min_price = min(min_price, p[i])
    if min_price == 10**9:
        print(-1)
        return
    print(min_price)

=======
Suggestion 8

def getMinMoney(n, a, p, x):
    minMoney = -1
    for i in range(n):
        if x[i] > 0:
            money = p[i]
            if minMoney == -1:
                minMoney = money
            else:
                minMoney = min(minMoney, money)
    return minMoney

=======
Suggestion 9

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
    ans = 1000000000
    for i in range(N):
        if X[i] > 0:
            ans = min(ans, P[i])
    if ans == 1000000000:
        ans = -1
    print(ans)

solve()

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
    min_price = 10**9
    for i in range(N):
        if X[i] > 0:
            min_price = min(min_price, P[i])
    if min_price == 10**9:
        print(-1)
    else:
        print(min_price)
