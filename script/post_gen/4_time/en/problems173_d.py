Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        ans += A[(i+1)//2]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    if n == 2:
        ans = a[0] + a[1]
    else:
        a.sort()
        ans = a[-1] + a[-2]
        for i in range(n - 3):
            ans += a[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * (N - i) - 1)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N - 1):
        total += A[i]
    print(total)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[1::2]))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[1::2]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:N-2]))

main()

=======
Suggestion 9

def get_max_comfort(n, a):
    a = [0] + a + [0]
    max_comfort = 0
    for i in range(1, n + 1):
        max_comfort += min(a[i], a[i + 1])
    return max_comfort
