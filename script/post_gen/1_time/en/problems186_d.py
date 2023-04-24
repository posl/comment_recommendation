Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1) - A[i] * i
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1) - a[i] * i
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * i - sum(A[:i])
        ans += sum(A[i+1:]) - A[i] * (N - i - 1)

    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (i * A[i]) - ((N - i - 1) * A[i])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    sum = 0
    for i in range(0, N):
        sum += A[i] * (i+1) - A[i] * (N-i-1)
    print(sum)

=======
Suggestion 8

def sum_abs_diffs(arr):
    arr.sort()
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i] * (2*i - n + 1)
    return sum

n = int(input())
arr = list(map(int, input().split()))
print(sum_abs_diffs(arr))

=======
Suggestion 9

def get_ints(): return map(int, input().strip().split())
