Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
        return
    print(sum(H[K:]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    k = min(n-1, k)
    ans = sum(h[k:])
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort()
    if n <= k:
        print(0)
    else:
        print(sum(h[:n-k]))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    h.sort(reverse=True)

    if k >= n:
        print(0)
        return

    for i in range(k):
        h[i] = 0

    print(sum(h))

main()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 8

def main():
    #N, K = map(int, input().split())
    #H = list(map(int, input().split()))
    N, K = 3, 1
    H = [4, 1, 5]
    #N, K = 8, 9
    #H = [7, 9, 3, 2, 3, 8, 4, 6]
    #N, K = 3, 0
    #H = [1000000000, 1000000000, 1000000000]

    H.sort()
    H.reverse()
    #print(H)
    print(sum(H[K:]))

=======
Suggestion 9

def main():
    # N,K = map(int,input().split())
    # H = list(map(int,input().split()))
    # H.sort()
    # H.reverse()
    # print(sum(H[K:]))
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort()
    H.reverse()
    ans = 0
    for i in range(K,N):
        ans += H[i]
    print(ans)
main()
