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
    ans = 10**10
    for i in range(N):
        if A[i] < X[i]:
            ans = min(ans, P[i])
    if ans == 10**10:
        ans = -1
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
    ans = -1
    for i in range(N):
        if X[i] > A[i]:
            if ans == -1:
                ans = P[i]
            else:
                ans = min(ans, P[i])
    print(ans)

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
    result = -1
    for i in range(N):
        if X[i] > A[i]:
            if result == -1:
                result = P[i]
            else:
                result = min(result, P[i])
    print(result)

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

    ans = 10**9 + 1
    for i in range(N):
        if X[i] - A[i] > 0:
            ans = min(ans, P[i])
    if ans == 10**9 + 1:
        print(-1)
    else:
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

    min_price = 10**10
    for i in range(N):
        if X[i] > A[i]:
            min_price = min(min_price, P[i])
    if min_price == 10**10:
        min_price = -1

    print(min_price)

=======
Suggestion 6

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
    ans = 10**9
    for i in range(N):
        if X[i] - A[i] > 0:
            ans = min(ans, P[i])
    if ans == 10**9:
        ans = -1
    print(ans)
main()

=======
Suggestion 7

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
    ans = 1000000000
    for i in range(N):
        if X[i] > 0:
            ans = min(ans,P[i])
    if ans == 1000000000:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = list(map(int, input().split()))
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 1000000000000000000
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 1000000000000000000:
        ans = -1
    print(ans)
main()

=======
Suggestion 9

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
    ans = 9999999999999999999
    for i in range(n):
        if x[i] > 0:
            ans = min(ans, p[i])
    if ans == 9999999999999999999:
        ans = -1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    ans = 10000000000
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10000000000:
        ans = -1
    print(ans)
