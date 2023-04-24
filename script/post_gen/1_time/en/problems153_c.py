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
    h.sort(reverse=True)
    for i in range(k):
        h[i] = 0
    print(sum(h))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(sum(h[:n-k]))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    print(sum(h[k:]))

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort()
    print(sum(H[:max(0,N-K)]))
