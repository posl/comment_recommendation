Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] = max(0, b[i] - a[i])
        ans += min(a[i+1], b[i])
        a[i+1] = max(0, a[i+1] - b[i])

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        ans += min(A[i+1], B[i] - min(A[i], B[i]))

    ans += min(A[N], B[N-1])

    print(ans)

main()

=======
Suggestion 3

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        if A[i+1] > B[i]:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
        else:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i] -= min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
        b[i] -= min(a[i+1], b[i])
    print(ans)

=======
Suggestion 5

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
                b[i] -= a[i+1]
            else:
                ans += b[i]
                a[i+1] -= b[i]
        else:
            ans += b[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        if A[i+1] > B[i]:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
        else:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += B[i]
            A[i] -= B[i]
        else:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] > B[i]:
                ans += B[i]
                A[i+1] -= B[i]
            else:
                ans += A[i+1]
                A[i+1] = 0
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            if A[i+1] <= B[i] - A[i]:
                count += A[i+1]
                A[i+1] = 0
            else:
                count += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
        else:
            count += B[i]
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if a[i] > b[i]:
            count += b[i]
            a[i] -= b[i]
        else:
            count += a[i]
            b[i] -= a[i]
            a[i] = 0
            if a[i+1] > b[i]:
                count += b[i]
                a[i+1] -= b[i]
            else:
                count += a[i+1]
                a[i+1] = 0

    print(count)
