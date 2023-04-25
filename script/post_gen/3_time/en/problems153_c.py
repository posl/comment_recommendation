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
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse = True)
    if N <= K:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(sum(h[:-k]) if k < n else 0)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:max(0, N-K)]))
