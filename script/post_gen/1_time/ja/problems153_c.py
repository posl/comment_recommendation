Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

main()

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
    ans = 0
    for i in range(N):
        if i < K:
            continue
        ans += H[i]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse = True)
    if N <= K:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:max(0, N - K)]))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:-K]) if N > K else 0)
