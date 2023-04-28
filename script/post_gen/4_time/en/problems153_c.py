Synthesizing 10/10 solutions

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
    if K == 0:
        print(sum(H))
    else:
        print(sum(H[K:]))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = sorted([int(x) for x in input().split()], reverse=True)
    if K > N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    h = sorted(map(int, input().split()), reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

=======
Suggestion 6

def problems153_c():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    if K > N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 7

def solve():
    N,K=map(int,input().split())
    H=list(map(int,input().split()))
    H.sort()
    if K>=N:
        print(0)
        return
    print(sum(H[:N-K]))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    h = sorted(list(map(int,input().split())),reverse=True)
    print(sum(h[k:]))

=======
Suggestion 9

def problems153_c():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    #print(H)
    if K == 0:
        print(sum(H))
    else:
        print(sum(H[:-K]))

=======
Suggestion 10

def get_ints(): return map(int, sys.stdin.readline().strip().split())
