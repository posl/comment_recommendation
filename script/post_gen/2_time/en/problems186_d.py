Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (N-i-1)*A[i] - i*A[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] - i * A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1]) * i * (N-i)
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i - (N - i - 1))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()

    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - 1 - i)

    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    left = 0
    right = sum(A)
    ans = 0
    for i in range(N):
        left += A[i]
        right -= A[i]
        ans += A[i] * (N - i - 1) - (right - left)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(abs(A[0] - A[1]))
        return
    A.sort()
    L = A[:N//2]
    R = A[N//2:]
    Lsum = sum(L)
    Rsum = sum(R)
    Llen = len(L)
    Rlen = len(R)
    print((Rsum - Lsum) * 2 - R[0] + L[-1] + (Rlen - Llen) * (R[0] - L[-1]))

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_acc = list(accumulate(A))
    A_acc_r = list(accumulate(A[::-1]))[::-1]
    ans = 0
    for i in range(N-1):
        ans += (i+1)*A[i] - A_acc[i] + A_acc_r[i+1] - (N-i-1)*A[i+1]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # sort a
    a.sort()

    # compute the sum of |a_i-a_j| for all pairs (i, j) where 1 <= i < j <= n
    ans = 0
    for i in range(n - 1):
        ans += (n - i - 1) * a[i]
        ans -= i * a[i]

    print(ans)
