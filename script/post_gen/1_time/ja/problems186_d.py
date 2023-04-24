Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * i - a[i] * (n - i - 1)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i * 2 - n + 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * (2 * i - N + 1)
    print(sum)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i - (N - i - 1))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i - (n - 1 - i))
    print(ans * 2)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (A[N-1-i] - A[i]) * (N-1-i-i)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i]*i - a[i]*(n-i-1)
    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(n):
        ans += a[i] * (2*i - n + 1)

    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * (N - 1 - i)
        ans -= A[i] * i
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]

    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * (2*i - N + 1)
    print(ans)
