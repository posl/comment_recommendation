Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * i - a[i] * (n - i - 1)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i]*(2*i-n+1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += i * A[i] - (N - i) * A[i-1]
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - 1 - i) - a[i] * i
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i] * (n - i - 1) - a[i] * i
    print(sum)

=======
Suggestion 7

def solve(N, A):
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1) - A[i] * i
    return ans

=======
Suggestion 8

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1)
    for i in range(n):
        ans -= a[i] * i
    print(ans * 2)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s = 0
    for i in range(N):
        s += (A[i] - A[0]) * (2 * i - N + 1)
    print(s)
