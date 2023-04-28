Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        if l*r <= 0:
            ans = min(ans, min(abs(l), abs(r))*2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] >= 0:
            ans = min(ans,max(abs(x[i]),abs(x[i+k-1])))
        else:
            ans = min(ans,abs(x[i])+abs(x[i+k-1])+min(abs(x[i]),abs(x[i+k-1])))
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        ans = min(ans, min(abs(l), abs(r)) + r - l)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    ans = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        if left*right<=0:
            ans = min(ans, abs(left)*2+abs(right))
        else:
            ans = min(ans, max(abs(left), abs(right)))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(X[i])+abs(X[i+K-1]-X[i]), abs(X[i+K-1])+abs(X[i+K-1]-X[i])))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1]-x[i]+min(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        if X[i] <= 0 and X[i+K-1] <= 0:
            ans = min(ans, abs(X[i]))
        elif X[i] <= 0 and X[i+K-1] >= 0:
            ans = min(ans, 2*abs(X[i])+X[i+K-1])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, abs(X[i+K-1]))
    print(ans)

=======
Suggestion 8

def main():
    from sys import stdin
    readline = stdin.readline
    N, K = map(int, readline().split())
    X = list(map(int, readline().split()))
    ans = 10 ** 18
    for i in range(N - K + 1):
        ans = min(ans, min(abs(X[i + K - 1] - X[i]) + abs(X[i]), abs(X[i + K - 1] - X[i]) + abs(X[i + K - 1])))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    # 1本のろうそくに火を付けるのに必要な最小の時間
    min_time = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        time = min(abs(left), abs(right)) + abs(right-left)
        if time < min_time:
            min_time = time

    print(min_time)

=======
Suggestion 10

def solve(n,k,x):
  ans = 10**9
  for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    if l*r >= 0:
      ans = min(ans,max(abs(l),abs(r)))
    else:
      ans = min(ans,abs(l)+r+min(abs(l),abs(r)))
  return ans

n,k = map(int,input().split())
x = list(map(int,input().split()))
print(solve(n,k,x))
