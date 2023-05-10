Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 2

def get_min_price(n, k, x, a):
    a.sort()
    price = 0
    for i in range(n):
        if k > 0:
            price += max(a[i]-x, 0)
            k -= 1
        else:
            price += a[i]
    return price

=======
Suggestion 3

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
                K -= 1
            else:
                ans += X
        else:
            ans += A[i]
    print(ans)
    return 0

=======
Suggestion 4

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if k > 0:
            if a[i] >= x:
                ans += x
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 5

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    total = 0
    for i in range(n):
        if k > 0:
            if a[i] > x:
                total += x
                k -= 1
            else:
                total += a[i]
        else:
            total += a[i]
    print(total)

=======
Suggestion 6

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
                K -= 1
            else:
                ans += X
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 7

def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(0,a[i]-x)
    print(ans)

=======
Suggestion 8

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
                K -= 1
            else:
                ans += X
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N-K]) + max(0, X * K - sum(A[:N-K])))

=======
Suggestion 10

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    ans = 0
    for i in range(N):
        if K > 0:
            K -= 1
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]

    print(ans)
