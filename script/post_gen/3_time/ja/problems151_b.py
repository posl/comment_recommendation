Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum <= k:
        print(max(n*m - sum, 0))
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n*m - sum(a) <= k:
        print(max(0, n*m - sum(a)))
    else:
        print(-1)

=======
Suggestion 3

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum > k:
        print(-1)
    elif n*m - sum < 0:
        print(0)
    else:
        print(n*m - sum)

=======
Suggestion 4

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    ans = -1
    for i in range(k + 1):
        if (sum_a + i) / n >= m:
            ans = i
            break
    print(ans)

=======
Suggestion 5

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    score = m * n - sum(a)
    if score <= k:
        if score < 0:
            print(0)
        else:
            print(score)
    else:
        print(-1)

=======
Suggestion 6

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if (m * n) - sum_a > k:
        print(-1)
    else:
        print((m * n) - sum_a if (m * n) - sum_a > 0 else 0)

=======
Suggestion 7

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N * M <= total:
        print(0)
    elif N * M - total <= K:
        print(N * M - total)
    else:
        print(-1)

=======
Suggestion 8

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    target = N * M
    if target - total > K:
        print(-1)
    else:
        print(max(target - total, 0))

=======
Suggestion 9

def solve():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = n*m - s
    if ans > k:
        print(-1)
    elif ans < 0:
        print(0)
    else:
        print(ans)

=======
Suggestion 10

def is_ok(mid):
    sum = 0
    for i in range(N-1):
        sum += A[i]
    sum += mid
    if sum / N >= M:
        return True
    else:
        return False
