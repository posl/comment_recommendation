Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    ans = sum(h)
    for i in range(k):
        ans -= h[i]
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    ans = sum(H[K:])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    H.reverse()
    print(sum(H[K:]))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    #print(H)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

main()

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if k >= n:
        print(0)
        return
    print(sum(h[:-k - 1]))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

main()

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort()
    if n <= k:
        print(0)
        return
    print(sum(h[:n-k]))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(sum(h[:n-k]))
