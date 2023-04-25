Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(1, N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2 * i * (N - i)

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1]) ** 2
    ans *= N - 1
    for i in range(1, N-1):
        ans -= 2 * (A[i] - A[i-1]) * (A[i+1] - A[i])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, N):
        ans += (i * A[i] - sum(A[:i])) ** 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] ** 2 - i * A[i] ** 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_a2 = sum([i**2 for i in a])
    ans = 0
    for i in range(n):
        sum_a -= a[i]
        sum_a2 -= a[i]**2
        ans += (n - 1 - i) * a[i]**2 + 2 * a[i] * sum_a - sum_a2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a2 = [x**2 for x in a]
    s2 = sum(a2)
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        s2 -= a2[i]
        ans += s2 - 2 * s * a[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_sq_a = sum([x*x for x in a])
    ans = 0
    for i in range(n):
        sum_a -= a[i]
        sum_sq_a -= a[i] * a[i]
        ans += sum_sq_a - 2 * a[i] * sum_a
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    #print(a)
    sum = 0
    for i in range(1, n + 1):
        sum += i * (a[i] ** 2)
    #print(sum)
    for i in range(1, n + 1):
        sum -= 2 * a[i] * (sum_a(a, i, n))
    print(sum)
