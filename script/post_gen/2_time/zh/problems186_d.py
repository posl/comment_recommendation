Synthesizing 10/10 solutions

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
    sum = 0
    for i in range(n):
        sum += a[i] * (2 * i - n + 1)
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += (A[i] * (2*i-N+1))
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += a[i] - a[i - 1]
    print(ans * 2)

=======
Suggestion 5

def solve(n, a):
    # Write your code here
    a.sort()
    sum = 0
    for i in range(n):
        sum += (2*i-n+1)*a[i]
    return sum

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += S - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    a_list.sort()
    sum = 0
    for i in range(n):
        sum += a_list[i] * (n-i-1) - a_list[i] * i
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] - a[0]) * (i - (n - i - 1))
    print(ans * 2)
