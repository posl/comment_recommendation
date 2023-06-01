Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a)>k:
        print(-1)
    else:
        print(max(0,n*m-sum(a)))

=======
Suggestion 2

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a)>k:
        print(-1)
    elif n*m-sum(a)<=0:
        print(0)
    else:
        print(n*m-sum(a))

=======
Suggestion 3

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) <= k and n*m-sum(a) >= 0:
        print(n*m-sum(a))
    else:
        print(-1)

=======
Suggestion 4

def get_input():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, m, a

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    elif N * M - sum(A) < 0:
        print(0)
    else:
        print(N * M - sum(A))
main()

=======
Suggestion 6

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) <= k:
        print(max(n * m - sum(a), 0))
    else:
        print(-1)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N*M-sum(A) <= K:
        print(max(0, N*M-sum(A)))
    else:
        print(-1)

=======
Suggestion 8

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if n * m - sum_a > k:
        print(-1)
    else:
        print(max(n * m - sum_a, 0))
