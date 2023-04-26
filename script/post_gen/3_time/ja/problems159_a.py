Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 + M * (M - 1) // 2)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    print(n * (n - 1) // 2 + m * (m - 1) // 2)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    print(n*(n-1)//2 + m*(m-1)//2)

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    print(int(N*(N-1)/2 + M*(M-1)/2))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        print(0)
        return
    if N == 1 and M == 1:
        print(0)
        return
    if N == 1:
        print(M - 1)
        return
    if M == 1:
        print(N - 1)
        return
    print(N * M - N - M)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    if N > M:
        N,M = M,N
    #print(N,M)
    if N == 0:
        print(M)
        return
    ans = N*(M-N) + N*(N-1)//2
    print(ans)
