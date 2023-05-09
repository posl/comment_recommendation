Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] ** 2 * (n - 1)
    for i in range(1, n):
        ans -= 2 * a[i - 1] * sum(a[i:])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        ans += (A[i + 1] - A[i]) ** 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1])**2
    print(ans)
    return

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1]) ** 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += sum([(a[i] - a[j])**2 for j in range(i)])
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]**2
    ans *= N-1
    for i in range(N-1):
        ans -= 2*A[i]*(sum(A[i+1:]))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (i * a[i]**2 - 2 * a[i] * sum(a[:i]) + sum(a[:i]) ** 2)
    print(ans)
