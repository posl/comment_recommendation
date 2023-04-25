Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    result = 0
    for i in range(N):
        if A[i] <= B[i]:
            result += A[i]
            if A[i+1] <= B[i] - A[i]:
                result += A[i+1]
                A[i+1] = 0
            else:
                result += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
        else:
            result += B[i]
    print(result + min(A[-1], B[-1]))

=======
Suggestion 2

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
            else:
                ans += B[i]
                A[i+1] -= B[i]
        else:
            ans += B[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                count += A[i+1]
                A[i+1] = 0
            else:
                count += B[i]
                A[i+1] -= B[i]
        else:
            count += B[i]
    count += A[N]
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        if a[i+1] > b[i]:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
        else:
            ans += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    for i in range(N):
        if A[i] <= B[i]:
            result += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                result += A[i+1]
                A[i+1] = 0
            else:
                result += B[i]
                A[i+1] -= B[i]
        else:
            result += B[i]
    print(result)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            if a[i+1] <= b[i] - a[i]:
                ans += a[i+1]
                a[i+1] = 0
            else:
                ans += b[i] - a[i]
                a[i+1] -= b[i] - a[i]
        else:
            ans += b[i]
    ans += min(b[n], a[n])
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            count += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            count += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            count += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] <= B[i]:
            total += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                total += A[i+1]
                B[i] -= A[i+1]
            else:
                total += B[i]
                A[i+1] -= B[i]
        else:
            total += B[i]
    print(total)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if A[i] >= B[i]:
            cnt += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            cnt += A[i]
            B[i] -= A[i]
            A[i] = 0
        if A[i+1] >= B[i]:
            cnt += B[i]
            A[i+1] -= B[i]
            B[i] = 0
        else:
            cnt += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
    print(cnt)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(min(b[i], a[i]))
        c.append(min(b[i+1], a[i]-c[i]))
    print(sum(c))
