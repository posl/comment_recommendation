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
        ans += ((1 / N) * ((1 / 2) ** cnt))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += 1 / N * 0.5 ** cnt
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
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += 1/N * (1/2)**cnt
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
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1/N) * (1/2)**cnt
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - K) * (K - 1) * 6 + (N - 1) * 3 + 1)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(1, N + 1):
        p = 1 / N
        j = i
        while j < K:
            j *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(1, N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        result += (1 / N) * (1 / 2) ** cnt
    print(result)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - K + 1) / (N * N))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - K + 1) * (N - K + 1) / N / N)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print((N - 2) * (K - 1) / (N * N))
