Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + p[i] / p[i - 1]
    ans = 0
    for i in range(k, n + 1):
        ans = max(ans, s[i] - s[i - k])
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = sum(p[:k]) + sum(p[-k:])
    print(ans/2)

=======
Suggestion 3

def main():
    return

=======
Suggestion 4

def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i]+p[i]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans,(s[i+K]-s[i])/2+(s[i]+s[i+K])/2/K)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    sum_p = sum(p[0:k])
    max_sum_p = sum_p
    for i in range(k, n):
        sum_p = sum_p + p[i] - p[i-k]
        if sum_p > max_sum_p:
            max_sum_p = sum_p
    print((max_sum_p + k) / 2)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += P[i]
    ans += K
    ans /= 2
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k, n):
        sum += p[i] - p[i-k]
        if sum > max:
            max = sum
    print((max+k)/2)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    maxsum = 0
    for i in range(k):
        maxsum += p[i]
    sum = maxsum
    for i in range(k,n):
        sum = sum - p[i-k] + p[i]
        if sum > maxsum:
            maxsum = sum
    print((maxsum + k)/2)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    m = s
    for i in range(K, N):
        s += p[i] - p[i-K]
        if s > m:
            m = s
    print((m + K) / 2)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[-k:]) / 2 ** k)
