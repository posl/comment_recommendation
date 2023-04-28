Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = n % k
    if ans > k:
        ans = k - ans
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    ans = n
    while True:
        if ans > abs(ans-k):
            ans = abs(ans-k)
        else:
            print(ans)
            exit()

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    if n == 0:
        print(0)
        return
    if k == 1:
        print(0)
        return
    if n < k:
        print(n)
        return
    r = n % k
    print(min(r,abs(r-k)))

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    while True:
        if n < k:
            break
        else:
            n = n % k
            if n == 0:
                break
            else:
                n = abs(n-k)
    print(n)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = N % K
    print(min(ans, abs(ans - K)))

main()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    n = n % k
    print(min(n,abs(n-k)))
