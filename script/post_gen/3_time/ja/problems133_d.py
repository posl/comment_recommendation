Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i % 2 == 0:
            ans[0] += A[i]
        else:
            ans[0] -= A[i]
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    print(" ".join(map(str, ans)))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i % 2 == 0:
            ans[0] += A[i]
        else:
            ans[0] -= A[i]
    for i in range(1, N):
        ans[i] = (A[i - 1] - ans[i - 1] // 2) * 2
    print(*ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, n):
        ans[i] = 2 * a[i-1] - ans[i-1]
    print(' '.join(map(str, ans)))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*n
    for i in range(n):
        if i%2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]
    for i in range(1,n):
        ans[i] = 2*a[i-1] - ans[i-1]
    print(*ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - sum(a[1::2]) * 2
    for i in range(1, n):
        b[i] = a[i-1] * 2 - b[i-1]
    print(" ".join(map(str, b)))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(n-1):
        ans[i+1] = 2 * a[i] - ans[i]
    print(*ans)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, N):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    print(*ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            print(A[1] + A[N-1], end=' ')
        elif i == N-1:
            print(A[N-2] + A[0], end=' ')
        else:
            print(A[i-1] + A[i+1], end=' ')

=======
Suggestion 9

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(A[i] - (sum(A) - A[i]))
        else:
            ans.append(A[i] - (A[i - 1]))
    print(*ans)

=======
Suggestion 10

def main():
    # input
    n = int(input())
    a = [int(i) for i in input().split()]
    # compute
    b = [0] * n
    b[0] = a[0]
    for i in range(1,n):
        b[i] = a[i] - b[i-1] // 2
    b[0] = a[0] - b[-1] // 2
    # output
    print(" ".join([str(i) for i in b]))
