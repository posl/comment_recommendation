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
    min_price = 10**18
    for i in range(N):
        if A[i] < X[i]:
            min_price = min(min_price, P[i])
    if min_price == 10**18:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0]*N
    P = [0]*N
    X = [0]*N
    for i in range(N):
        A[i], P[i], X[i] = map(int, input().split())
    minp = 10**9+1
    for i in range(N):
        if X[i]-A[i] > 0:
            minp = min(minp, P[i])
    if minp == 10**9+1:
        print(-1)
    else:
        print(minp)

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for n in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 10 ** 9 + 1
    for n in range(N):
        if X[n] - A[n] > 0:
            min_price = min(min_price, P[n])
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)

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

def main():
    N = int(input())
    ans = 10**9+1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X-A > 0:
            ans = min(ans, P)
    if ans == 10**9+1:
        print(-1)
    else:
        print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    ans = 10**9
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            ans = min(ans, P)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    shop = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shop.append([A, P, X])
    shop.sort(key=lambda x: x[0])
    for a, p, x in shop:
        if x - a > 0:
            print(p)
            return
    print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    answer = []
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            answer.append(P)
    if answer:
        print(min(answer))
    else:
        print(-1)

=======
Suggestion 9

def main():
    N = int(input())
    min_price = 10**9+1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X-A > 0:
            min_price = min(min_price, P)
    if min_price == 10**9+1:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 10

def main():
    N = int(input())
    shop = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shop.append([A, P, X])

    shop.sort(key=lambda x: x[1])

    for i in range(N):
        if shop[i][2] - shop[i][0] > 0:
            print(shop[i][1])
            return
    print(-1)
