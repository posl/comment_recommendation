Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if (l<=0 and r<=0) or (l>=0 and r>=0):
            ans = min(ans, max(abs(l), abs(r)))
        else:
            ans = min(ans, min(abs(l), abs(r))+r-l)
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        ans = min(ans, min(abs(l)+r-l, abs(r)+r-l))
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] < 0:
            ans = min(ans, max(abs(x[i]), abs(x[i+k-1])) + x[i+k-1] - x[i])
        else:
            ans = min(ans, max(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i]*x[i+K-1] > 0:
            ans = min(ans, max(abs(x[i]), abs(x[i+K-1])))
        else:
            ans = min(ans, abs(x[i])+abs(x[i+K-1])+min(abs(x[i]), abs(x[i+K-1])))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n - k + 1):
        if x[i] < 0 and x[i + k - 1] < 0:
            ans = min(ans, -x[i])
        elif x[i] < 0 and x[i + k - 1] >= 0:
            ans = min(ans, -x[i] * 2 + x[i + k - 1])
        else:
            ans = min(ans, x[i + k - 1])
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        right = x[i+k-1]
        left = x[i]
        ans = min(ans, right-left+min(abs(left), abs(right)))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    print(min(2*abs(x[i])+abs(x[i+K-1]) for i in range(N-K+1)))

=======
Suggestion 8

def main():
  n,k = map(int,input().split())
  x = list(map(int,input().split()))
  ans = float('inf')
  for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    if l <= 0 and r <= 0:
      ans = min(ans,abs(l))
    elif l <= 0 and r >= 0:
      ans = min(ans,abs(l)*2+r,abs(r)*2+abs(l))
    else:
      ans = min(ans,abs(r))
  print(ans)
main()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, x[i + K - 1] - x[i] + min(abs(x[i]), abs(x[i + K - 1])))
    print(ans)

=======
Suggestion 10

def main():
    # Get the input
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    # Find the minimum time required to light K candles
    min_time = min(abs(x[i]) * 2 + abs(x[i] - x[i + k - 1]) for i in range(n - k + 1))
    # Print the minimum time required to light K candles
    print(min_time)
