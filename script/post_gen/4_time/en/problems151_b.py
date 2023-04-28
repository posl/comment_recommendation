Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) > K:
        print(-1)
    else:
        print(max(M * N - sum(A), 0))

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    elif N * M - sum(A) < 0:
        print(0)
    else:
        print(N * M - sum(A))

=======
Suggestion 3

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) <= k:
        print(max(n * m - sum(a), 0))
    else:
        print(-1)

main()

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N*M-sum(A) > K:
        print(-1)
    else:
        print(max(0, N*M-sum(A)))

=======
Suggestion 5

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n*m-sum(a)>k:
        print(-1)
    else:
        print(max(n*m-sum(a),0))

=======
Suggestion 6

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    score = 0
    for i in range(N-1):
        score += A[i]
    if score >= M*N:
        print(0)
    elif score + K >= M*N:
        print(M*N - score)
    else:
        print(-1)

=======
Suggestion 7

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a)>k:
        print(-1)
    else:
        print(max(0,n*m-sum(a)))

=======
Suggestion 8

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if m*n - sum(a) > k:
        print(-1)
    else:
        print(max(0,m*n-sum(a)))

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if sum_A >= M * N:
        print(0)
    elif sum_A + K < M * N:
        print(-1)
    else:
        print(M * N - sum_A)

=======
Suggestion 10

def main():
    #input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    #compute
    sum_A = sum(A)
    if N*M > sum_A + K:
        print(-1)
    else:
        if N*M - sum_A > 0:
            print(N*M - sum_A)
        else:
            print(0)
