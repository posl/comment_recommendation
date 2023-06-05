Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        else:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        if a[i+1] <= b[i]:
            ans += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
        else:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    #print('N = ',N)
    #print('A = ',A)
    #print('B = ',B)
    sum = 0
    for i in range(N):
        if A[i] <= B[i]:
            sum += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            sum += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            sum += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            sum += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(A[i], B[i])
        if A[i] > B[i]:
            A[i] -= B[i]
            B[i] = 0
        else:
            B[i] -= A[i]
            A[i] = 0
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1] - B[i])
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
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        if a[i+1] >= b[i]:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
        else:
            ans += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0

        if A[i+1] >= B[i]:
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
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total = 0
    for i in range(n):
        if b[i] >= a[i]:
            total += a[i]
            b[i] -= a[i]
            if b[i] >= a[i+1]:
                total += a[i+1]
                b[i] -= a[i+1]
            else:
                total += b[i]
                b[i+1] -= b[i]
        else:
            total += b[i]

    print(total)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        c = min(a[i], b[i])
        ans += c
        a[i] -= c
        b[i] -= c
        d = min(a[i+1], b[i])
        ans += d
        a[i+1] -= d
        b[i] -= d
    print(ans)
