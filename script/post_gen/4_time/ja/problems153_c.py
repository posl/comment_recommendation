Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

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
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if k >= n:
        print(0)
    else:
        print(sum(h[:n-k]))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    cnt = 0
    for i in range(K,N):
        cnt += H[i]
    print(cnt)

=======
Suggestion 8

def solve():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)

    ans = 0
    for i in range(K, N):
        ans += H[i]

    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    H = H[K:]

    print(sum(H))

main()
