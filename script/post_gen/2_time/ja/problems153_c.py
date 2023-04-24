Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if N <= K:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = 0
    for i in range(N-K):
        ans += H[i]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            continue
        ans += H[i]
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    ans = sum(h[k:])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = 0
    if K > 0:
        ans = sum(H[:-K])
    else:
        ans = sum(H)
    print(ans)
