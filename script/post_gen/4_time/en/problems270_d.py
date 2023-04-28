Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if i == 0:
            ans += A[i]
        else:
            ans += A[i] * (N // A[i] - N // A[i-1])
    print(ans)

=======
Suggestion 2

def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  stones = [0] * (N + 1)
  for i in range(1, N + 1):
    for a in A:
      if i >= a:
        stones[i] = (stones[i] + stones[i - a]) % 1000000007
      elif a > i:
        break
    if i in A:
      stones[i] = (stones[i] + 1) % 1000000007
  print(stones[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if A[i] <= N:
            ans += A[i]
            N -= A[i]
        else:
            break
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    takahashi = 0
    aoki = 0
    for i in range(K):
        if i == 0:
            takahashi = A[i] - 1
        elif i == K-1:
            takahashi = max(takahashi, N - A[i-1])
        else:
            takahashi = max(takahashi, A[i] - A[i-1])
    print(takahashi)

=======
Suggestion 5

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(K-1,-1,-1):
        if N >= A[i]:
            ans += N // A[i]
            N = N % A[i]
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0,0)
    ans = 0
    for i in range(1,k+1):
        if a[i] > n:
            break
        else:
            ans += n // a[i]
            n = n % a[i]
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum(A[:A.index(N)]))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    stone = [1] * (N+1)
    for i in range(2, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if stone[i-A[j]] == 1:
                    stone[i] = 0
                    break
    for i in range(N, 0, -1):
        if stone[i] == 0:
            for j in range(K):
                if i - A[j] >= 0:
                    stone[i-A[j]] = 1
    print(sum(stone))

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(K):
        if A[i] >= N:
            print(N)
            exit()
    ans = 0
    while N > 0:
        ans += N%A[0]
        N = N//A[0]*A[0]
        if N == 0:
            break
        while A[-1] > N:
            A.pop()
    print(ans)

=======
Suggestion 10

def problem():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A = sorted(A)
    #print(A)
    result = 0
    for i in range(K+1):
        #print(A[i], A[i+1])
        result += (A[i+1] - A[i] - 1) // (i+1)
    print(result)
