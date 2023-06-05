Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = sum(H)
    for i in range(K):
        ans -= H[i]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort()
    if k >= n:
        print(0)
    else:
        print(sum(h[:n-k]))

main()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort()
    for i in range(K):
        H.pop()

    print(sum(H))

main()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    if k>=n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:N-K]))

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    ans = sum(h)
    if k > n - 1:
        k = n - 1
    ans -= sum(h[:k])
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))
