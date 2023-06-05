Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*M-sum(A) <= K:
        print(max(0,N*M-sum(A)))
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))
    if n * m - sum(A) > k:
        print(-1)
    else:
        print(max(0, n * m - sum(A)))

=======
Suggestion 3

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) <= k:
        print(max(0, n * m - sum(a)))
    else:
        print(-1)

=======
Suggestion 4

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) > k:
        print(-1)
    elif n*m-sum(a) < 0:
        print(0)
    else:
        print(n*m-sum(a))

=======
Suggestion 5

def func(n, k, m, a):
    if n * m - sum(a) > k:
        return -1
    else:
        return max(0, n * m - sum(a))

=======
Suggestion 6

def main():
    N,K,M = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    if N*M-sum(A)>K:
        print(-1)
    else:
        print(max(N*M-sum(A),0))

=======
Suggestion 7

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if (N * M - sum(A)) > K:
        print(-1)
    else:
        print(max(0, N * M - sum(A)))

=======
Suggestion 8

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        print(max(N * M - sum(A), 0))
    else:
        print(-1)

=======
Suggestion 9

def main():
    n,k,m=map(int,input().split())
    a=list(map(int,input().split()))
    if n*m-sum(a)>k:
        print(-1)
    else:
        print(max(n*m-sum(a),0))

=======
Suggestion 10

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*M-sum(A) > K:
        print(-1)
    else:
        print(max(N*M-sum(A),0))
