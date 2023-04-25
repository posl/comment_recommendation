Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, abs(N % K - K)))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - N % K))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - (N % K)))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)
main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans-K))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ans = min(N%K, abs(N%K-K))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    ans = min(N % K, K - N % K)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(min(N % K, abs(N % K - K)))
