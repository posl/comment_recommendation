Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - A[i-1]
    print(*B)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = [0] * n
    for i in range(n):
        result[i] = a[i] - (a[i] // 2) * 2
    for i in range(n):
        if i == n - 1:
            print(result[i] + result[0])
        else:
            print(result[i] + result[i + 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    ans[0] = sum(A) - sum(A[1::2])*2
    for i in range(1, N):
        ans[i] = A[i-1]*2 - ans[i-1]
    print(*ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * n
    for i in range(n):
        d[(i-1) % n] += a[i]
        d[(i+1) % n] += a[i]
    print(*d)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n
    ans[0] = sum(a) - 2 * sum(a[1::2])

    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]

    print(*ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        if i%2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    #print(B)
    for i in range(1,N):
        B[i] = 2*A[i-1] - B[i-1]
    #print(B)
    print(*B)
    return 0

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[i] = A[i]*2
    for i in range(N-1):
        ans[i+1] -= ans[i]
    print(*ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = (A[i-1] - B[i-1] // 2) * 2
    print(' '.join(map(str, B)))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - b[i - 1]
    print(*b)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = 2 * A[i-1] - B[i-1]
    print(' '.join(map(str, B)))
