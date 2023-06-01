Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:N - K]))

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    ans = 0
    if k >= n:
        print(ans)
    else:
        for i in range(k,n):
            ans += h[i]
        print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 4

def attack_num(h, k):
    h.sort(reverse=True)
    return sum(h[k:])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    total = sum(h)
    if k >= n:
        print(0)
    else:
        print(total - sum(h[-k-1:]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(sum(h[:n-k]))

=======
Suggestion 9

def main():
    N,K=map(int,input().split())
    H=list(map(int,input().split()))

    H.sort(reverse=True)
    #print(H)

    if K>=N:
        print(0)
    else:
        print(sum(H[K:]))

main()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = 0
    for i in range(K, N):
        ans += H[i]
    print(ans)
