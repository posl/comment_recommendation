Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    ans = sum(h)
    for i in range(k):
        ans -= h[i]
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 4

def solve(n, k, h):
    h.sort(reverse=True)
    ans = sum(h)
    for i in range(k):
        ans -= h[i]
    return ans

n, k = map(int, input().split())
h = list(map(int, input().split()))

print(solve(n, k, h))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H = sorted(H,reverse=True)
    if K >= N:
        print(0)
        return
    else:
        print(sum(H[K:]))

=======
Suggestion 7

def solve(N, K, H):
    H.sort()
    #print(H)
    print(sum(H[:-K]) if K < N else 0)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))
