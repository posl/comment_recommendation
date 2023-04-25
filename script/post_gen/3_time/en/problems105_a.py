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
    n, k = [int(x) for x in input().split()]
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    if N % K != 0:
        ans = 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(N % K)

=======
Suggestion 5

def main():
    # read input
    N, K = map(int, input().split())

    # calculate
    if N % K == 0:
        ans = 0
    else:
        ans = 1

    # print output
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    print(n%k)
