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
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j])**2
    print(ans)
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2
    for i in range(1, N - 1):
        ans -= 2 * (A[i] - A[i - 1]) * (A[i + 1] - A[i])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1])**2
    for i in range(1, N-1):
        ans -= 2*(A[i+1] - A[i])*(A[i] - A[i-1])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += (a[i] - a[i-1]) ** 2
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    print(sum([sum([(a[i] - a[j])**2 for j in range(i)]) for i in range(1, n)]))
