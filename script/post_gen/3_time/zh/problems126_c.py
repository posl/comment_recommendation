Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        tmp = i
        cnt = 0
        while tmp<k:
            tmp *= 2
            cnt += 1
        ans += (1/n) * (0.5 ** cnt)
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1 / N
        else:
            j = 0
            while i * (2 ** j) < K:
                j += 1
            ans += (1 / N) * (0.5 ** j)
    print(ans)

=======
Suggestion 3

def problem126_c(N, K):
    if N >= K:
        return 1
    elif N == 1:
        return 1 / K
    else:
        return (1 / N) * (1 / 2) ** (len(bin(K - 1)) - 2)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            point = 1
            while i * point < K:
                point *= 2
            ans += 1 / point
    print(ans / N)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        cnt = 0
        score = i
        while score < k:
            score *= 2
            cnt += 1
        ans += 1 / n * 0.5 ** cnt
    print(ans)

=======
Suggestion 7

def solve(n, k):
    if n >= k:
        return 1.0
    elif n * 2 >= k:
        return (n + 1.0) / (2 * n)
    else:
        return 1.0 * (n + 1 - k) / (n - k + 1) + (k - 1) * 2.0 / (n - k + 1)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        score = i
        p = 1/n
        while score < k:
            score *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    prob = 0
    for i in range(1, N + 1):
        if i >= K:
            prob += 1 / N
        else:
            prob += (1 / N) * (1 / 2) ** (len(bin(K - 1 - i)) - 2)
    print(prob)
