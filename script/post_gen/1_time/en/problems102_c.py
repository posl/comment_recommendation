Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 1:
        ans = 0
        for i in range(n):
            ans += abs(b[i] - b[n // 2])
        print(ans)
    else:
        ans1 = 0
        for i in range(n):
            ans1 += abs(b[i] - b[n // 2])
        ans2 = 0
        for i in range(n):
            ans2 += abs(b[i] - b[n // 2 - 1])
        print(min(ans1, ans2))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 1:
        m = b[n // 2]
    else:
        m = (b[n // 2] + b[n // 2 - 1]) // 2
    ans = 0
    for i in range(n):
        ans += abs(b[i] - m)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 0:
        print(b[n // 2] - b[n // 2 - 1] + 1)
    else:
        print(b[n // 2] - b[n // 2] + 1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[i] - (i+1) for i in range(n)]
    b.sort()
    if n % 2 == 1:
        x = b[n//2]
    else:
        x = (b[n//2-1] + b[n//2]) // 2
    print(sum([abs(b[i]-x) for i in range(n)]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - i - 1)
    b.sort()
    if n % 2 == 1:
        median = b[n // 2]
    else:
        median = (b[n // 2] + b[n // 2 - 1]) // 2
    ans = 0
    for i in range(n):
        ans += abs(b[i] - median)
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [a[i] - i - 1 for i in range(n)]
    a.sort()
    b = a[n//2]
    print(sum([abs(a[i]-b) for i in range(n)]))

solve()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i] - (i+1)
    sum = abs(sum)
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    for i in range(N):
        b += A[i] - i - 1
    A.sort()
    b1 = b
    b2 = b
    if N % 2 == 0:
        b1 -= A[int(N/2)] - int(N/2)
        b2 -= A[int(N/2)-1] - int(N/2)
    else:
        b1 -= A[int(N/2)] - int(N/2)
        b2 -= A[int(N/2)] - int(N/2)
    print(min(abs(b1), abs(b2)))

=======
Suggestion 10

def min_sadness(a):
    b = sum(a) // len(a)
    return sum(abs(a[i] - (b + i + 1)) for i in range(len(a)))
