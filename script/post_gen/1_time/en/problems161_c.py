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
    ans = N % K
    print(min(ans, K - ans))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if N < K:
        print(N)
    else:
        print(N % K)
