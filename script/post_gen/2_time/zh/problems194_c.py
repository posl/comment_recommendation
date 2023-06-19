Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    s = 0
    for i in range(1, n):
        s += (a[i] - a[i-1]) * (a[i] - a[i-1]) * (n - i) * i
    return s

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(n):
        ans += a[i] ** 2 * (n - 1)
        ans -= 2 * a[i] * (s[n] - s[i + 1])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 5

def solve(N, A):
    sum = 0
    for i in range(1, N):
        for j in range(0, i):
            sum += (A[i] - A[j]) ** 2
    return sum

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    sum_a = sum(a)
    for i in range(n):
        sum_a -= a[i]
        ans += (n-1)*a[i]**2 - 2*a[i]*sum_a
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += (A[i]-A[j])**2
    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += a[i] * a[i]
        ans -= 2 * a[i] * sum(a[:i])
        ans += sum(a[:i]) * sum(a[:i])
    print(ans)

solve()

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += (a[i] - a[i-1]) ** 2
    for i in range(1, n-1):
        ans -= 2 * (a[i] - a[i-1]) * (a[i+1] - a[i])
    print(ans)
