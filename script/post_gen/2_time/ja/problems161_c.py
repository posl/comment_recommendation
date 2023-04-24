Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans - K))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(N % K)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    #print(n,k)
    if n%k == 0:
        print(0)
    else:
        print(1)
