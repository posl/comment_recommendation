Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - N % K))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans - K))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans-K))
    print(ans)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = N % K
    print(min(ans, abs(ans - K)))

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    cnt = 0
    while N>0:
        N = N%K
        cnt += 1
    print(cnt-1)
