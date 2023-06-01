Synthesizing 10/10 solutions

=======
Suggestion 1

def problem126_c(n,k):
    if n>k:
        return 1/(2**(n-k))
    else:
        return 0.5

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        elif i < k:
            x = i
            while x < k:
                x *= 2
            p += 1/n * (0.5 ** (x/i))
    print(p)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1 / n) * (1 / (2 ** cnt))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        score = i
        p = 1 / N
        while score < K:
            score *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 5

def solve(n, k):
    ans = 0
    for i in range(1, n + 1):
        p = 1
        while i < k:
            i *= 2
            p /= 2
        ans += p
    return ans / n

n, k = map(int, input().split())
print(solve(n, k))

=======
Suggestion 6

def solve(n,k):
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            cnt = 0
            while i < k:
                i *= 2
                cnt += 1
            ans += (1/n) * (0.5 ** cnt)
    return ans

=======
Suggestion 7

def solve():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += 1/n*(1/2)**(len(bin(k-i))-3)
    print(ans)

=======
Suggestion 8

def solve():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        p = 1
        while i<K:
            i *= 2
            p /= 2
        ans += p
    print(ans/N)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        else:
            j = 1
            while i * 2 ** j < k:
                j += 1
            p += (1/2) ** j / n
    print(p)

=======
Suggestion 10

def solve():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1 / n) * (0.5 ** cnt)
    print(ans)
