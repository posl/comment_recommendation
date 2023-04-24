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
        if X[i] - A[i] > 0:
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
    min_price = 1000000001
    for i in range(N):
        if X[i] - A[i] > 0:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == 1000000001:
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
        A_i, P_i, X_i = map(int, input().split())
        A.append(A_i)
        P.append(P_i)
        X.append(X_i)
    ans = -1
    for i in range(N):
        if X[i] > A[i]:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = -1
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            if ans == -1:
                ans = P
            else:
                ans = min(ans, P)
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = -1
    for i in range(N):
        if X[i] - A[i] > 0:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if a < x:
            if ans == -1 or ans > p:
                ans = p
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 10**10
    for _ in range(n):
        a, p, x = map(int, input().split())
        if x - a > 0:
            ans = min(ans, p)
    if ans == 10**10:
        ans = -1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append([A, P, X])
    shops.sort(key=lambda x: x[0])
    for shop in shops:
        if shop[2] - shop[0] > 0:
            return shop[1]
    return -1

print(main())

=======
Suggestion 9

def main():
    N = int(input())
    min_price = -1
    for n in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            if min_price == -1:
                min_price = P
            elif min_price > P:
                min_price = P
    print(min_price)

=======
Suggestion 10

def get_input():
    n = int(input())
    shops = []
    for _ in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    return shops
