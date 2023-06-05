Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, k = map(int, input().split())

    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += 1 / n * (1 / 2) ** cnt

    print(ans)

solve()

=======
Suggestion 2

def solve(n,k):
    p = 0
    for i in range(1,n+1):
        t = 0
        while i < k:
            i *= 2
            t += 1
        p += (1/n)*(1/2)**t
    return p

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    if k <= n:
        print(1/2)
    else:
        ans = 0
        for i in range(1,n+1):
            if i >= k:
                ans += 1/n
            else:
                x = 1
                while i * x < k:
                    x *= 2
                ans += (1/2)**x
        print(ans/n)

=======
Suggestion 4

def problem126_c():
    pass

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    count = 0
    for i in range(1,n+1):
        if i >= k:
            count += 1/n
        else:
            count += (1/n) * ((1/2)**(len(bin(k)[2:])-1))
    print(count)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = 0
    for i in range(1, n+1):
        j = 0
        while i * (2 ** j) < k:
            j += 1
        p += (1/n) * (1/2) ** j
    print(p)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        if i >= k:
            result += 1/n
        else:
            result += (1/n)*(1/2)**(i.bit_length()-1)
    print(result)
main()

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        x = 1
        while i < k:
            i *= 2
            x *= 0.5
        ans += x
    ans /= n
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    total = 0
    for i in range(1, N + 1):
        if i >= K:
            total += 1
        else:
            total += 1 / 2 ** (len(bin(K - 1)) - 2)
    print(total / N)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        point = i
        count = 0
        while point < K:
            point *= 2
            count += 1
        ans += (1 / N) * ((1 / 2) ** count)
    print(ans)
