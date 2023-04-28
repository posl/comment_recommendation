Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        if i >= k:
            ans += 1 / n
        else:
            cnt = 0
            while i < k:
                i *= 2
                cnt += 1
            ans += (1 / n) * (0.5 ** cnt)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1 / n) * (1 / (2 ** cnt))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1 / N
        else:
            ans += 1 / N * (1 / 2) ** (len(bin(K - 1)[2:]) - len(bin(i)[2:]))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1/2)**cnt/N
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += 1/N * 0.5**cnt
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1 / N
            continue
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1 / N) * ((1 / 2) ** cnt)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        count = 0
        while i < K:
            i *= 2
            count += 1
        ans += 1/N * (1/2)**count
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(n):
        x = i + 1
        cnt = 0
        while x < k:
            x *= 2
            cnt += 1
        ans += (1 / (2 ** cnt)) / n
    print(ans)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            tmp = 0
            while i < K:
                i *= 2
                tmp += 1
            ans += (1 / N) * (0.5 ** tmp)
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    ans = 0.0
    for i in range(1,N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1/N)*(0.5**cnt)
    print(ans)
