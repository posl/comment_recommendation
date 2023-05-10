Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * i
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i//2]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i // 2]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = 0
    for i in range(1, n):
        ans += a[i//2]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    for i in range(N):
        ans = max(ans, sum(A[i:i+N:2]))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a + a
    t = sum(a[:n])
    ans = t
    for i in range(n):
        t = t + a[n + i] - a[i]
        ans = max(ans, t)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i * 2 + 1]
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i//2]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    s = sum(a)
    mx = 0
    for i in range(n):
        mx = max(mx, s - a[i] - a[i + 1] - a[i + 2])
    print(mx)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += a[i]
        else:
            ans += min(a[i], a[i-1])
    ans += min(a[0], a[-1])
    print(ans)
