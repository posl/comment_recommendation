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
    ans = []
    for i in range(N):
        if A[i] < X[i]:
            ans.append(P[i])
    if ans:
        print(min(ans))
    else:
        print(-1)

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
    ans = -1
    for i in range(N):
        if X[i] - A[i] > 0:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

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
    minp = 10**10
    for i in range(N):
        if A[i] < X[i]:
            minp = min(minp, P[i])
    if minp == 10**10:
        print(-1)
    else:
        print(minp)

=======
Suggestion 4

def main():
    N = int(input())
    A, P, X = [], [], []
    for _ in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 10**9
    for i in range(N):
        if X[i] - A[i] > 0:
            min_price = min(min_price, P[i])
    if min_price == 10**9:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 10**10
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            ans = min(ans, P)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    ans = 10**9+1
    for i in range(N):
        A,P,X = map(int,input().split())
        if X-A > 0:
            ans = min(ans,P)
    if ans == 10**9+1:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    min_price = 10**9
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            min_price = min(min_price, P)
    if min_price == 10**9:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 8

def main():
    N = int(input())
    P = []
    for i in range(N):
        A, B, C = map(int, input().split())
        if C > 1:
            P.append([A, B])
    if len(P) == 0:
        print(-1)
        return
    P.sort()
    print(P[0][1])

=======
Suggestion 9

def main():
    N = int(input())
    P = []
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            P.append([P, X])
    if len(P) == 0:
        print(-1)
    else:
        print(min(P)[0])

=======
Suggestion 10

def main():
    n = int(input())
    stock = [list(map(int, input().split())) for _ in range(n)]
    stock.sort()
    for i in range(n):
        if stock[i][2] - stock[i][0] > 0:
            print(stock[i][1])
            return
    print(-1)
