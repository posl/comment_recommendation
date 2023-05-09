Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)

    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    if k >= n:
        print(0)
        exit()
    for i in range(k):
        h[i] = 0
    print(sum(h))

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    h = sorted(map(int, input().split()), reverse=True)
    print(sum(h[k:]))

=======
Suggestion 7

def main():
    N, K = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    H.sort()
    H.reverse()
    print(sum(H[K:]))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    H = [int(h) for h in input().split()]
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))
