Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        ans += min(A[i+1], B[i])
        A[i+1] -= min(A[i+1], B[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] -= min(a[i], b[i])

        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0

        if A[i+1] <= B[i]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
        else:
            ans += B[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
        else:
            ans += a[i]
            if a[i+1] >= b[i] - a[i]:
                ans += b[i] - a[i]
                a[i+1] -= b[i] - a[i]
            else:
                ans += a[i+1]
                a[i+1] = 0

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            if a[i+1] <= b[i]:
                ans += a[i+1]
                a[i+1] = 0
            else:
                ans += b[i]
                a[i+1] -= b[i]
        else:
            ans += b[i]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] - b[i] >= 0:
            ans += b[i]
            a[i] -= b[i]
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
            if a[i+1] - b[i] >= 0:
                ans += b[i]
                a[i+1] -= b[i]
            else:
                ans += a[i+1]
                a[i+1] = 0

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    num = 0
    for i in range(N):
        if B[i] >= A[i]:
            num += A[i]
            B[i] = B[i] - A[i]
            if B[i] >= A[i+1]:
                num += A[i+1]
                A[i+1] = 0
            else:
                num += B[i]
                A[i+1] = A[i+1] - B[i]
        else:
            num += B[i]
    print(num)
