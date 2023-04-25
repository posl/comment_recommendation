Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    left = 0
    right = 10**12 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if sum((a - 1) // mid for a in A) <= K:
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-K+1):
        ans += A[i] * A[N-i-1]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(0, N, K):
        ans += A[i]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == K:
        print(1)
        return
    if K == 1:
        print(N)
        return
    if A[-1] == 1:
        print(N)
        return
    if A[0] == A[-1]:
        print(1)
        return
    if A[0] == 1:
        print(N - A.count(1))
        return
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if A[0] == A[1]:
        print(1)
        return
    if A[1] == A[2]:
        print(2)
        return
    if A[-1] == A[-2]:
        print(N - 1)
        return
    if A[-2] == A[-3]:
        print(N - 2)
        return
    if N == 4:
        print(2)
        return
    if A[0] == A[1] and A[1] == A[2]:
        print(1)
        return
    if A[1] == A[2] and A[2] == A[3]:
        print(2)
        return
    if A[-1] == A[-2] and A[-2] == A[-3]:
        print(N - 1)
        return
    if A[-2] == A[-3] and A[-3] == A[-4]:
        print(N - 2)
        return
    if N == 5:
        print(2)
        return
    if A[0] == A[1] and A[1] == A[2] and A[2] == A[3]:
        print(1)
        return
    if A[1] == A[2] and A[2] == A[3] and A[3] == A[4]:
        print(2)
        return
    if A[-1] == A[-2] and A[-2] == A[-3] and A[-3] == A[-4]:
        print(N - 1)
        return
    if A[-2]

=======
Suggestion 5

def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort()
    if K == N:
        print(1)
        return
    if K == 1:
        print(A[-1])
        return
    if K == 2:
        print(A[-1] + A[-2])
        return
    # K >= 3
    # A[0] - 1, A[1] - 2, A[2] - 3, ... A[N-K] - (N-K)
    # A[N-K] - (N-K) + A[N-K+1] - (N-K+1) + ... + A[N-1] - (N-1)
    # (A[N-K] + A[N-K+1] + ... + A[N-1]) - (N-K) - (N-K+1) - ... - (N-1)
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    left = 0
    right = n - 1
    while left < right:
        if a[left] + a[right] < k:
            left += 1
        else:
            ans += right - left
            right -= 1
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, a[i] * a[n-k+i])
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        print(n)
        return
    if n == k:
        print(1)
        return
    if a[0] == a[-1]:
        print(1)
        return
    if a[0] == a[k-1]:
        print(n - k + 1)
        return
    if a[k-1] == a[k]:
        print(n - k + 1)
        return
    if a[k-1] < a[k]:
        print(1)
        return
    if a[k-1] > a[k]:
        print(2)
        return

=======
Suggestion 9

def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if i < k:
            ans += a[i]
        else:
            ans += a[i] - 1
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    print(A[K-1])

main()
