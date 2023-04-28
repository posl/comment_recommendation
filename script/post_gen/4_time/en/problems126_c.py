Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1 / N) * (1 / 2) ** cnt
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N + 1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1/N) * (1/2)**cnt
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        x = i
        while x < K:
            x *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        j = i
        while j < K:
            p = p/2
            j *= 2
        ans += p
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N + 1):
        tmp = 1 / N
        j = i
        while j < K:
            tmp *= 1 / 2
            j *= 2
        ans += tmp
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        c = 0
        while i < K:
            i *= 2
            c += 1
        ans += (1/N) * (1/2)**c
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ans = 0.0
    for i in range(1, N + 1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1 / N) * (1 / 2) ** cnt
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N-K)*(K-1)*6 + (N-1)*3 + 1)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    if k == 1:
        print(0)
        return
    if n == 1:
        print(1)
        return
    ret = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ret += (1 / n) * ((1 / 2) ** cnt)
    print(ret)

=======
Suggestion 10

def solve(N, K):
    if K == 1:
        return 0
    if N >= K:
        return (N - K + 1) / N
    return (N - K + 1) / N + (K - 1) / N * (K - 1) / N * solve(N, K - 1)
