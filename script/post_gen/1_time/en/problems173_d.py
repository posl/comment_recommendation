Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i // 2]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i]
    ans += a[-1] // 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * (i // 2)
        ans += A[i - 1] * ((i + 1) // 2)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * (N - i) - 1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        return
    A.sort()
    print(A[-1] + sum(A[:-1]))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * 2 ** (i - 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:-1]))

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i]
    ans -= n - 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    print(sum(A[:-1]))
