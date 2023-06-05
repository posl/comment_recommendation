Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    ans = N*M - sum
    if ans > K:
        print(-1)
    else:
        print(max(ans, 0))

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = N * M - S
    if ans > K:
        print(-1)
    elif ans < 0:
        print(0)
    else:
        print(ans)

=======
Suggestion 3

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    t = m * n - sum(a)
    if t > k:
        print(-1)
    elif t < 0:
        print(0)
    else:
        print(t)

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    else:
        print(max(N * M - sum(A), 0))

=======
Suggestion 5

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*M-sum(A) <= K:
        print(max(N*M-sum(A),0))
    else:
        print(-1)

=======
Suggestion 6

def main():
    # input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    # process
    score = N*M - sum(A)
    if score > K:
        score = -1
    elif score < 0:
        score = 0
    # output
    print(score)

=======
Suggestion 7

def main():
    # 读取输入
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    # 计算
    min_score = m*n - sum(a)
    if min_score < 0:
        print(0)
    elif min_score <= k:
        print(min_score)
    else:
        print(-1)

=======
Suggestion 8

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) > k:
        print(-1)
    else:
        print(max(n * m - sum(a), 0))

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    else:
        print(max(0, N * M - sum(A)))

=======
Suggestion 10

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    if n * m <= s:
        print(0)
    elif n * m - s <= k:
        print(n * m - s)
    else:
        print(-1)
