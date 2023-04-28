Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += (a[i] - a[j]) ** 2
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i):
            sum += (a[i] - a[j])**2
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (n - 1) * a[i] ** 2
    for i in range(1, n):
        ans -= 2 * a[i] * sum(a[:i])
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1,n):
        for j in range(0,i):
            sum += (a[i]-a[j])**2
    print(sum)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += sum([(A[i] - A[j])**2 for j in range(i)])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(sum([sum([(a[i] - a[j]) ** 2 for j in range(i)]) for i in range(1, n)]))

=======
Suggestion 7

def solve(n, a):
    ans = 0
    for i in range(n):
        ans += a[i] * a[i] * (n - 1)
    for i in range(n - 1):
        ans -= 2 * a[i] * sum(a[i + 1:])
    return ans

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = sum(a)
    s = 0
    for i in range(n):
        t -= a[i]
        s += t*a[i]
    print(s)

=======
Suggestion 9

def sum_of_squared_differences(N, A):
    sum = 0
    for i in range(1,N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    return sum

=======
Suggestion 10

def solve(n, a):
  ans = 0
  for i in range(n):
    ans += (n - 1) * a[i] ** 2
  for i in range(n - 1):
    ans -= 2 * (n - i - 1) * a[i] * sum(a[i + 1:])
  return ans
