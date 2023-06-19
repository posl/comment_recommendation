Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, M, A

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m * n - sum(a) > k:
        print(-1)
    else:
        print(max(m * n - sum(a), 0))

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = M * N - sum(A)
    if X > K:
        print(-1)
    elif X < 0:
        print(0)
    else:
        print(X)

=======
Suggestion 4

def solve(n,k,m,a):
    sum = 0
    for i in range(n-1):
        sum += a[i]
    x = n*m - sum
    if x>k:
        return -1
    elif x<0:
        return 0
    else:
        return x
n,k,m = map(int,input().split())
a = list(map(int,input().split()))
print(solve(n,k,m,a))

=======
Suggestion 5

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    score = sum(A)
    if score >= M*(N-1):
        print(M*N-score)
    else:
        print(-1)

=======
Suggestion 6

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) > k:
        print(-1)
    else:
        print(max(0,n*m-sum(a)))

=======
Suggestion 7

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*K-sum(A)<0:
        print(0)
    elif N*K-sum(A)>M:
        print(-1)
    else:
        print(N*K-sum(A))

=======
Suggestion 8

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if N * M - sum > K:
        print(-1)
    else:
        print(N * M - sum)

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        print(max(0, N * M - sum(A)))
    else:
        print(-1)

=======
Suggestion 10

def get_input():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    return n,k,m,a
