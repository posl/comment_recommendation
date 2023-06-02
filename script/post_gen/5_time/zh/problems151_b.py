Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        print(max(N * M - sum(A), 0))
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) > k:
        print(-1)
    else:
        print(max(n * m - sum(a), 0))

=======
Suggestion 3

def solve(N, K, M, A):
    # write code here
    # N, K, M = map(int, input().split())
    # A = list(map(int, input().split()))
    # N = 4
    # K = 100
    # M = 60
    # A = [0, 0, 0]
    # N = 5
    # K = 10
    # M = 7
    # A = [8, 10, 3, 6]
    # N = 4
    # K = 100
    # M = 60
    # A = [100, 100, 100]
    # N = 2
    # K = 100
    # M = 60
    # A = [100]
    # N = 2
    # K = 100
    # M = 60
    # A = [60]
    # N = 2
    # K = 100
    # M = 60
    # A = [59]
    # N = 2
    # K = 100
    # M = 60
    # A = [58]
    # N = 2
    # K = 100
    # M = 60
    # A = [57]
    # N = 2
    # K = 100
    # M = 60
    # A = [56]
    # N = 2
    # K = 100
    # M = 60
    # A = [55]
    # N = 2
    # K = 100
    # M = 60
    # A = [54]
    # N = 2
    # K = 100
    # M = 60
    # A = [53]
    # N = 2
    # K = 100
    # M = 60
    # A = [52]
    # N = 2
    # K = 100
    # M = 60
    # A = [51]
    # N = 2
    # K = 100
    # M = 60
    # A = [50]
    # N = 2
    # K = 100
    # M

=======
Suggestion 4

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n * m - sum(a)
    if ans < 0:
        print(0)
    elif ans > k:
        print(-1)
    else:
        print(ans)
main()

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    ans = -1
    for i in range(K+1):
        if (s + i) / N >= M:
            ans = i
            break
    print(ans)

=======
Suggestion 6

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    if n*m - sum_a > k:
        print(-1)
    else:
        print(max(n*m - sum_a,0))

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        print(max(0, N * M - sum(A)))
    else:
        print(-1)

=======
Suggestion 8

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n * m - sum(a) > k:
        print(-1)
    else:
        print(max(0,n*m-sum(a)))

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    elif N * M - sum(A) <= 0:
        print(0)
    else:
        print(N * M - sum(A))

=======
Suggestion 10

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if n * m - sum_a <= k:
        print(max(n * m - sum_a, 0))
    else:
        print(-1)
