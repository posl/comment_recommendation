Synthesizing 10/10 solutions

=======
Suggestion 1

def buy_play_snuke():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    flag = 0
    min_price = 10**9
    for j in range(n):
        if x[j] > 0:
            if p[j] < min_price:
                min_price = p[j]
                flag = 1
    if flag == 0:
        return -1
    else:
        return min_price

=======
Suggestion 2

def buy_snuke(N, A, P, X):
    min_price = 1000000000
    for i in range(N):
        if X[i] > 0:
            if P[i] < min_price:
                min_price = P[i]
    return min_price

=======
Suggestion 3

def solve():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append([A, P, X])

    min_cost = -1
    for i in range(N):
        A, P, X = shops[i]
        if X > 0:
            if min_cost == -1:
                min_cost = P
            else:
                min_cost = min(min_cost, P)

    print(min_cost)

=======
Suggestion 4

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

def solve(N, A, P, X):
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1 or result > P[i]:
                result = P[i]
    return result

=======
Suggestion 7

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
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1:
                result = P[i]
            else:
                result = min(result, P[i])
    print(result)

=======
Suggestion 8

def buyPlaySnuke(n):
    minPrice = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if x > 0:
            if minPrice == -1:
                minPrice = p
            elif minPrice > p:
                minPrice = p
    print(minPrice)

=======
Suggestion 9

def getMinPrice(N, A, P, X):
    min_price = -1
    for i in range(N):
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            elif min_price > P[i]:
                min_price = P[i]
    return min_price

=======
Suggestion 10

def findMinPrice(N, A, P, X):
    minPrice = -1
    for i in range(N):
        if X[i] > 0:
            if minPrice == -1:
                minPrice = P[i]
            elif minPrice > P[i]:
                minPrice = P[i]
    return minPrice
