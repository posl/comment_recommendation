Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > x:
            ans += (a[i] - x)
    if k > ans:
        print(0)
    else:
        print(ans - k)

=======
Suggestion 2

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
Suggestion 3

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] - X > 0:
                ans += X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 4

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        if k > 0:
            sum += max(a[i] - x, 0)
            k -= 1
        else:
            sum += a[i]
    print(sum)

=======
Suggestion 5

def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= x:
            ans += a[i]
        else:
            ans += x
    print(ans)

=======
Suggestion 6

def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            if a[i] > x:
                ans += x
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 7

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if k > 0:
            if a[i] > x:
                ans += a[i] - x
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 8

def main():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    #print(N,K,X)
    #print(A)
    #print(A[0])

    sum = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                sum += A[i] - X
                K -= 1
            else:
                sum += A[i]
        else:
            sum += A[i]

    print(sum)

=======
Suggestion 9

def calcCost(a, x):
    if a <= x:
        return 0
    else:
        return a - x
