Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1/n)*(1/2)**cnt
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            p = 1
            while i < K:
                i *= 2
                p /= 2
            ans += p
    print(ans / N)

solve()

=======
Suggestion 3

def solve():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        tmp = 1
        while i < K:
            i *= 2
            tmp *= 0.5
        ans += tmp
    print(ans/N)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += (1/n)*((1/2)**(len(bin(k-i))-2))
    print(ans)

=======
Suggestion 5

def solve():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            point = 1
            while i*point < k:
                point *= 2
            ans += (1/n) * (1/point)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1/n) * (0.5 ** cnt)
    print(ans)

=======
Suggestion 7

def solve(N, K):
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        while i < K:
            i *= 2
            p /= 2
        ans += p
    return ans

=======
Suggestion 8

def solve(n, k):
    ans = 0
    for i in range(1, n+1):
        p = 1.0 / n
        while i < k:
            i *= 2
            p /= 2
        ans += p
    return ans

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        score = i
        p = 1/N
        while score < K:
            score *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        x = i
        cnt = 0
        while x < K:
            x *= 2
            cnt += 1
        ans += 1 / N * (1 / 2) ** cnt
    print(ans)

main()
