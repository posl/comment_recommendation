Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def solve():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1 / n) * (1 / 2) ** cnt
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        count = 0
        while i < k:
            i *= 2
            count += 1
        ans += (1/n) * (1/2)**count
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            ans += 1/N*(0.5)**(K/i)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = 0
    for i in range(1, n+1):
        if i >= k:
            p += 1/n
        else:
            p += 1/n * (1/2)**(len(bin(k-i))-2)
    print(p)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += 1/n * (1/2)**(len(bin(k-1))-2)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    prob = 0.0
    for i in range(1, N+1):
        if i >= K:
            prob += 1 / N
        else:
            prob += (1 / N) * (1 / 2) ** (len(bin(K - 1 - i)) - 2)
    print(prob)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    result = 0
    for i in range(1, n+1):
        if i >= k:
            result += 1/n
            continue
        count = 0
        while i < k:
            i *= 2
            count += 1
        result += (1/n) * (1/(2**count))
    print(result)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    #print(N, K)
    if K == 1:
        print(1)
        return
    if N >= K:
        print((N-K+1)/N)
        return
    else:
        #print((N-K+1)/N)
        #print(1/N)
        #print(1/K)
        print((N-K+1)/N + (1/N)*(1/2)*(K-N) + (1/N)*(1/2)*(N-1))
        return

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    if K <= N:
        print((K-1)/N)
        return
    else:
        print(((N-K+1)/N)**2*(K-1)/N*6)
        return
