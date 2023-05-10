Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        if i >= K:
            ans += 1/N
        else:
            count = 0
            while i < K:
                i *= 2
                count += 1
            ans += (1/N)*(1/2)**count
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            count = 0
            while i < K:
                i *= 2
                count += 1
            ans += (1/N) * (0.5**count)
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        score = i
        p = 1 / n
        while score < k:
            score *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(1)
        return
    if N >= K:
        print((K-1)/N)
        return
    else:
        print(((N-K+1)*2 + (K-1))/N**2)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i >= k:
            ans += 1/n
        else:
            cnt = 0
            while i < k:
                i *= 2
                cnt += 1
            ans += 1/n * 0.5**cnt
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    #print(N, K)
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            cnt = 0
            while i < K:
                i = i * 2
                cnt += 1
            ans += (1/N) * (1/(2**cnt))
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        count = 0
        while i < K:
            i *= 2
            count += 1
        ans += (1 / N) * (1 / 2) ** count
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1.0)
        return
    result = 0.0
    for i in range(1, N + 1):
        if i >= K:
            result += 1.0
        else:
            n = 1
            while i * 2 ** n < K:
                n += 1
            result += 1.0 / (N * 2 ** (n - 1))
    print(result)

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    ans = 0
    for i in range(1,n+1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1/pow(2,cnt))/n
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
        else:
            tmp = 1
            while i < K:
                i *= 2
                tmp /= 2
            ans += tmp / N
    print(ans)
