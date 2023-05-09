Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += 1/n * (1/2)**(len(bin(k-1))-2)
    print(ans)

=======
Suggestion 2

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
            ans += (1/2)**cnt/n
    print(ans)
main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        score = i
        cnt = 0
        while score < K:
            score *= 2
            cnt += 1
        ans += (1/N) * (1/2)**cnt
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
            x = i
            j = 0
            while x < K:
                x *= 2
                j += 1
            ans += (1/N) * (1/2)**j
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = 0
    for i in range(1, N+1):
        if i >= K:
            p += 1/N
        else:
            count = 0
            while i < K:
                i *= 2
                count += 1
            p += (1/N)*((1/2)**count)
    print(p)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())

    p = 0
    for i in range(1, n+1):
        if i >= k:
            p += 1/n
        else:
            j = 0
            while i * 2**j < k:
                j += 1
            p += (1/n) * (1/2)**j

    print(p)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1.0)
    else:
        n = N
        p = 1
        while n < K:
            n *= 2
            p /= 2
        print((N*p + (n-K+1)*p*2)/N)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        current = i
        p = 1/N
        if current >= K:
            ans += p
        else:
            while current < K:
                p /= 2
                current *= 2
            ans += p
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
    else:
        print((1/N)*((1/2)**(len(str(bin(K)[2:]))-1)))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    print(sum([(1/N)*((1/2)**i)*(1/2) for i in range(0,N) if 2**(i+1) >= K]))
