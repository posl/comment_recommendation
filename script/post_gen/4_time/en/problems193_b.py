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
    ans = 1000000000
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
    if ans == 1000000000:
        ans = -1
    print(ans)

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
    result = 1000000000000000000
    for i in range(N):
        if X[i] > A[i]:
            result = min(result, P[i])
    if result == 1000000000000000000:
        result = -1
    print(result)

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
    ans = 10000000000
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 10000000000:
        print(-1)
    else:
        print(ans)

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

    min_cost = 10**9
    for i in range(N):
        if X[i] > A[i]:
            min_cost = min(min_cost, P[i])

    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def solve():
    n = int(input())
    a = [0] * n
    p = [0] * n
    x = [0] * n
    for i in range(n):
        a[i], p[i], x[i] = map(int, input().split())
    ans = 10 ** 9 + 1
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10 ** 9 + 1:
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = list(map(int, input().split()))
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 1000000000
    for i in range(N):
        if X[i] > 0:
            min_price = min(min_price, P[i])
    if min_price == 1000000000:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 7

def main():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append([a, p, x])

    min_price = -1
    for i in range(n):
        if shops[i][2] > 0:
            if min_price == -1:
                min_price = shops[i][1]
            else:
                min_price = min(min_price, shops[i][1])
    print(min_price)

=======
Suggestion 8

def get_input():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append([a, p, x])
    return n, shops

=======
Suggestion 9

def solve():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    min_price = 1000000000
    for shop in shops:
        a, p, x = shop
        if x > 0:
            min_price = min(min_price, p)
    if min_price == 1000000000:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def main():
    # N = int(input())
    # shops = []
    # for _ in range(N):
    #     a, p, x = map(int, input().split())
    #     shops.append([a, p, x])
    # print(shops)
    # result = -1
    # for shop in shops:
    #     if shop[2] > 0:
    #         if result == -1:
    #             result = shop[1]
    #         elif shop[1] < result:
    #             result = shop[1]
    #         else:
    #             pass
    # print(result)

    N = int(input())
    A = []
    P = []
    X = []
    for _ in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1:
                result = P[i]
            elif P[i] < result:
                result = P[i]
            else:
                pass
    print(result)
