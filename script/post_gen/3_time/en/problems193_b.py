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
    for i in range(N):
        if A[i] < X[i]:
            print(P[i])
            return
    print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * N
    P = [0] * N
    X = [0] * N
    for i in range(N):
        A[i], P[i], X[i] = map(int, input().split())
    min_price = -1
    for i in range(N):
        if X[i] - A[i] > 0:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)

main()

=======
Suggestion 3

def main():
    n = int(input())
    ans = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if x - a > 0:
            if ans == -1:
                ans = p
            else:
                ans = min(ans, p)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = -1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X > A:
            if ans == -1:
                ans = P
            else:
                ans = min(ans, P)
    print(ans)
main()

I've been trying to solve this problem for a while now, and I'm not sure what I'm doing wrong. I've tried using the following code:

=======
Suggestion 5

def main():
    N = int(input())
    ans = 10**10
    for _ in range(N):
        A, P, X = map(int, input().split())
        if A < X:
            ans = min(ans, P)
    if ans == 10**10:
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
        a1,p1,x1 = map(int,input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)

    min = 1000000001
    for i in range(n):
        if a[i] < x[i]:
            if p[i] < min:
                min = p[i]

    if min == 1000000001:
        print(-1)
    else:
        print(min)

=======
Suggestion 7

def main():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    shops.sort(key=lambda x: x[0])
    ans = -1
    for A, P, X in shops:
        if X - A > 0:
            ans = P
            break
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    min_price = 10 ** 9 + 1
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0 and P < min_price:
            min_price = P
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)

main()

=======
Suggestion 9

def main():
    N = int(input())
    min_price = 10**9 + 1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            min_price = min(min_price, P)
    print(min_price if min_price < 10**9 + 1 else -1)

=======
Suggestion 10

def main():
    N = int(input())
    shops = [list(map(int, input().split())) for i in range(N)]
    ans = -1
    for i in range(N):
        if shops[i][0] < shops[i][2]:
            if ans == -1:
                ans = shops[i][1]
            else:
                ans = min(ans, shops[i][1])
    print(ans)
