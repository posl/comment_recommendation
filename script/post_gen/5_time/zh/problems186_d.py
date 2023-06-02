Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] - A[i-1]
    print(ans * 2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i - (n - i - 1))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        count += (i * a[i] - (n - i - 1) * a[i])
    print(count * 2)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (n - 1)
    b[0] = a[1] - a[0]
    for i in range(1, n - 1):
        b[i] = a[i + 1] - a[i]
    print(sum(b) * 2)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * (2 * i - N + 1)
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (A[i] - A[0]) * (N - i - 1)
        ans += (A[N - 1] - A[i]) * i
    print(ans)

=======
Suggestion 7

def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] * (2 * i - n + 1))
    return ans

=======
Suggestion 8

def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i * 2 - n + 1)
    return ans

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n):
        s += a[i] * i - a[i] * (n - i - 1)
    print(s)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2*i-n+1)
    print(ans)

main()
