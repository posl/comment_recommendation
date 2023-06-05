Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    sum = 0
    for i in range(n-k+1):
        tmp = 0
        for j in range(i,i+k):
            tmp += p[j]
        sum = max(sum,tmp)
    print((sum+k)/2)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0]
    for i in range(1, N + 1):
        s.append(s[i - 1] + p[i])
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (s[i + K] - s[i]) / 2 + s[i])
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p2 = [0]*(n+1)
    for i in range(n):
        p2[i+1] = p2[i] + p[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,(p2[i+k]-p2[i]+k)/2)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n - k):
        s = s - p[i] + p[i + k]
        if s > m:
            m = s
    print((m + k) / 2)

main()

=======
Suggestion 5

def solve(n, k, ps):
    ps = sorted(ps)
    s = sum(ps[-k:])
    return (s+k)/2

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0] * (n + 1)
    for i in range(n):
        p_sum[i + 1] = p_sum[i] + p[i]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (p_sum[i + k] - p_sum[i]) / 2 + p_sum[i])
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    sum = 0
    for i in p[n-k:n]:
        sum += i
    print((sum+k)/2)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    pl = list(map(int, input().split()))
    p_sum = sum(pl[:k])
    max_p_sum = p_sum
    for i in range(k, n):
        p_sum += pl[i] - pl[i-k]
        if p_sum > max_p_sum:
            max_p_sum = p_sum
    print((max_p_sum + k) / 2)

=======
Suggestion 9

def max_expected_value(n, k, p):
    s = sum(p[0:k])
    max_s = s
    for i in range(k, n):
        s += p[i] - p[i-k]
        max_s = max(max_s, s)
    return (max_s + k) / 2

=======
Suggestion 10

def main():
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  p = [0] + p
  s = [0] * (n + 1)
  for i in range(1, n + 1):
    s[i] = s[i - 1] + p[i]
  t = 0
  for i in range(n - k + 1):
    t = max(t, (s[i + k] - s[i]) / 2 + s[i])
  print(t)
