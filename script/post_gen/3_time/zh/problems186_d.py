Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = 0
    for i in range(n):
        s -= a[i]
        x += a[i] * s
    print(x)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i]
        ans -= i * A[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = a[0]
    y = a[-1]
    ans = 0
    for i in range(n):
        ans += (y-x)
        x = a[i]
        y = a[i+1]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * i - sum(a[:i])
        ans -= a[i] * (n - i - 1) - sum(a[i + 1:])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    A.sort()
    sum = 0
    for i in range(1, N):
        sum += A[i] - A[i-1]
    print(sum * 2)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r = n - 1
    ans = 0
    while l < r:
        ans += a[r] - a[l]
        r -= 1
        if l < r:
            ans += a[r] - a[l]
            l += 1
    print(ans)

=======
Suggestion 8

def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    return ans

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n):
        s += (a[i] * i - a[i] * (n - 1 - i))
    print(s)
