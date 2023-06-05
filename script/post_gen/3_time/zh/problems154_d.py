Synthesizing 10/10 solutions

=======
Suggestion 1

def problems154_d():
    pass

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort(reverse=True)
    max = 0
    for i in range(k):
        max += p[i]
    max += k
    print(max/2)
    return 0

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    max = 0
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k,n):
        sum = sum + p[i] - p[i-k]
        if max < sum:
            max = sum
    print((max+k)/2)

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    p_sum = [0]
    for i in range(1,n+1):
        p_sum.append(p_sum[i-1]+p[i])
    ans = 0
    for i in range(k, n+1):
        ans = max(ans, p_sum[i]-p_sum[i-k])
    print(ans/2)

=======
Suggestion 5

def main():
    # n, k = 5, 3
    # p = [1, 2, 2, 4, 5]
    n, k = 10, 4
    p = [17, 13, 13, 12, 15, 20, 10, 13, 17, 11]
    # n, k = 4, 1
    # p = [6, 6, 6, 6]
    # n, k = 4, 2
    # p = [6, 6, 6, 6]
    # n, k = 4, 3
    # p = [6, 6, 6, 6]
    # n, k = 4, 4
    # p = [6, 6, 6, 6]
    # n, k = 4, 3
    # p = [1, 2, 3, 4]
    # n, k = 4, 4
    # p = [1, 2, 3, 4]
    # n, k = 4, 2
    # p = [1, 2, 3, 4]
    # n, k = 4, 1
    # p = [1, 2, 3, 4]
    # n, k = 4, 3
    # p = [4, 3, 2, 1]
    # n, k = 4, 4
    # p = [4, 3, 2, 1]
    # n, k = 4, 2
    # p = [4, 3, 2, 1]
    # n, k = 4, 1
    # p = [4, 3, 2, 1]
    # n, k = 4, 3
    # p = [1, 1, 1, 1]
    # n, k = 4, 4
    # p = [1, 1, 1, 1]
    # n, k = 4, 2
    # p = [1, 1, 1, 1]
    # n

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p

    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + p[i]

    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (s[i + k] - s[i]) / 2 + s[i])

    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K])/2+0.5*K)
    print(ans)

=======
Suggestion 8

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
Suggestion 9

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [0] + P
    for i in range(1, N+1):
        P[i] += P[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (P[i+K] - P[i]) / 2 + P[i])
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    print(max([sum(p[i:i+k])*(p[i+k-1]+1)/2 for i in range(n-k+1)]))
