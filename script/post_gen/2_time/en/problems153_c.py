Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if n <= k:
        print(0)
    else:
        print(sum(h[:n-k]))

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if N <= K:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 5

def main():
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    h.sort()
    print(sum(h[:n-k]))

=======
Suggestion 6

def main():
    #input
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    #compute
    H.sort()
    ans = sum(H[:-K]) if N-K >= 0 else 0
    #output
    print(ans)
