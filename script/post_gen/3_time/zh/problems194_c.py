Synthesizing 10/10 solutions

=======
Suggestion 1

def problems194_c():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * a[i] * (n - 1)
    for i in range(n - 1):
        ans -= 2 * a[i] * sum(a[i + 1:n])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - 1)
    for i in range(N - 1):
        ans -= 2 * A[i] * sum(A[i + 1:])
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += (n - i) * (i) * (a[i] - a[i - 1]) ** 2
    print(ans)

=======
Suggestion 5

def sum_of_square_difference(A):
    return sum([sum([(A[i] - A[j]) ** 2 for j in range(i)]) for i in range(1, len(A))])

=======
Suggestion 6

def solve(n, a):
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(1, N):
        for j in range(0, i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 8

def solve(n, a):
    s = 0
    for i in range(1, n):
        for j in range(i):
            s += (a[i] - a[j]) ** 2
    return s

=======
Suggestion 9

def solve(N, A):
    ans = 0
    for i in range(1, N):
        for j in range(0, i):
            ans += (A[i] - A[j]) ** 2
    return ans

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ans += n * sum([i ** 2 for i in a])
    ans -= sum(a) ** 2
    print(ans)
