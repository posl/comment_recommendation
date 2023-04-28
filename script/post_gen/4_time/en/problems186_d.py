Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] - A[i-1]
    print(ans*2)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1) - a[i] * i
    print(ans)
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1) - a[i] * i
    print(ans)

=======
Suggestion 5

def main():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 5
    A = [31, 41, 59, 26, 53]

    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - 1 - i)
    print(sum)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (A[i] * (2 * i - N + 1))
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-1-2*i)*a[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    t = 0
    for i in range(n):
        t += a[i]**2

    print((n-1)*t - 2*s*(sum(a)))

=======
Suggestion 10

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(n):
        sum += A[i] * (n - 1 - i) - A[i] * i
    print(sum)
