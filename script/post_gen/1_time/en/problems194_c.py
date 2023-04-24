Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2
    ans *= N - 1
    for i in range(N):
        ans -= (A[i] * 2) ** 2
    print(ans // 2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (i * A[i] - sum(A[:i])) ** 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (N - i) * (A[i] - A[i - 1]) ** 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += (a[i] - a[j]) ** 2
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += (n - i) * a[i] * a[i]
        ans += i * a[i] * a[i]
    print(ans)

=======
Suggestion 7

def main():
    # Get input
    n = int(input())
    a = list(map(int, input().split()))
    # Calculate
    sum = 0
    for i in range(1, n):
        for j in range(i):
            sum += (a[i] - a[j]) ** 2
    # Output
    print(sum)

=======
Suggestion 8

def read_int():
    return int(input())
