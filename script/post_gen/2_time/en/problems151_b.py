Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= 0:
        print(0)
    elif N * M - sum(A) > K:
        print(-1)
    else:
        print(N * M - sum(A))

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    score = M * N - sum(A)
    if score < 0:
        print(-1)
    elif score > K:
        print(-1)
    else:
        print(score)

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + N * K >= N * M:
        print(max(0, N * M - sum(A)))
    else:
        print(-1)

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total / N >= M:
        print(0)
        return
    if (N-1) * K - total < M - total / N:
        print(-1)
        return
    print(M * N - total)

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if sum_A + K * (N - 1) < M * N:
        print(-1)
    else:
        print(max(0, M * N - sum_A))

=======
Suggestion 6

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    ave = m*n-sum(a)
    if ave <= 0:
        print(0)
    elif ave > k:
        print(-1)
    else:
        print(ave)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    if S >= M*N:
        print(0)
    elif S + K*(N-1) < M*N:
        print(-1)
    else:
        print(max(0, M*N-S))

=======
Suggestion 8

def main():
  n, k, m = map(int, input().split())
  a = list(map(int, input().split()))
  avg = m*n - sum(a)
  if avg <= 0:
    print(0)
  elif avg > k:
    print(-1)
  else:
    print(avg)

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, M)
    #print(A)
    score = sum(A)
    #print(score)
    required = M*N
    #print(required)
    if required - score <= K:
        if required - score < 0:
            print(0)
        else:
            print(required - score)
    else:
        print(-1)
