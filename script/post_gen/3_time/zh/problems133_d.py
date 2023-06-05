Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    x = [0] * n
    for i in range(n):
        x[i] = a[i] - sum(x) * 2
    return x

=======
Suggestion 2

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - sum(b) // 2
    return b

=======
Suggestion 3

def solve(n, a):
    b = [0] * n
    for i in range(0, n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    return b

n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a))

=======
Suggestion 4

def solve(n, a):
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]
    for i in range(1, n):
        ans[i] = 2 * a[i-1] - ans[i-1]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(' '.join(map(str, solve(n, a))))

=======
Suggestion 5

def solve(n, a):
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]
    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = 2 * A[i - 1] - B[i - 1]
    print(' '.join(map(str, B)))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    b[0] //= 2
    for i in range(n-1):
        b[i+1] = a[i] - b[i]
    print(*b)

=======
Suggestion 8

def solve(n, a):
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    return b

n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    print(' '.join(map(str, b)))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n

    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]

    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]

    print(' '.join(map(str, ans)))
