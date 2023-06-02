Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * (N + 1)
    for i in range(N):
        C[i] = A[i] - B[i]
        C[i + 1] = A[i + 1]
    ans = 0
    for i in range(N + 1):
        if C[i] > 0:
            ans += B[i]
        else:
            ans += A[i]
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
        if A[i] > B[i]:
            A[i] -= B[i]
            ans += min(A[i + 1], A[i])
            A[i + 1] -= A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    ans = 0
    for i in range(N):
        if B[i] >= A[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if B[i] >= A[i+1]:
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
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

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
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] < B[i]:
                ans += A[i+1]
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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(n):
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
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if b[i] >= a[i]:
            total += a[i]
            b[i] -= a[i]
            a[i] = 0
        else:
            total += b[i]
            a[i] -= b[i]
            b[i] = 0
        if b[i] >= a[i+1]:
            total += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
        else:
            total += b[i]
            a[i+1] -= b[i]
            b[i] = 0
    print(total)

=======
Suggestion 8

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
Suggestion 9

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    N = 2
    A = [3, 5, 2]
    B = [4, 5]
    # N = 3
    # A = [5, 6, 3, 8]
    # B = [5, 100, 8]
    # N = 2
    # A = [100, 1, 1]
    # B = [1, 100]
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
        if A[i + 1] <= B[i]:
            ans += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0
        else:
            ans += B[i]
            A[i + 1] -= B[i]
            B[i] = 0
    print(ans)
