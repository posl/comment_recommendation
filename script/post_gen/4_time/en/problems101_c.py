Synthesizing 10/10 solutions

=======
Suggestion 1

def problems101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if (n - 1) % (k - 1) == 0:
        print((n - 1) // (k - 1))
    else:
        print((n - 1) // (k - 1) + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-K):
        if A[i] < A[i+K]:
            cnt += 1
    print(cnt+1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print((N - 2) // (K - 1) + 1)

=======
Suggestion 4

def problem101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if (n - 1) % (k - 1) == 0:
        print((n - 1) // (k - 1))
    else:
        print((n - 1) // (k - 1) + 1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > 1:
        N -= K - 1
        count += 1
    print(count)
    return

=======
Suggestion 6

def problems101_c():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    if (n-1) % (k-1) == 0:
        ans = (n-1) // (k-1)
    else:
        ans = (n-1) // (k-1) + 1
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (a[i] - 1) // (k - 1)
    print(ans)

=======
Suggestion 8

def problems101_c():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    while N > K:
        N -= K - 1
        cnt += 1
    if N > 1:
        cnt += 1
    print(cnt)

problems101_c()

=======
Suggestion 9

def problems101_c(N, K, A):
    ans = 0
    while N > 0:
        N -= K
        ans += 1
    return ans

=======
Suggestion 10

def problem101_c():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    min_num = 0
    for i in range(N):
        if i == 0:
            min_num = A[i]
        else:
            if min_num > A[i]:
                min_num = A[i]
    print((N-1) // (K-1))

problem101_c()
