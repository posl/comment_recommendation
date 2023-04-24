Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    if L[M-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[M-1] + 1)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[-1] <= R[0]:
        print(R[0] - L[-1] + 1)
    else:
        print(0)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0]-L[-1]+1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    l = 0
    r = n + 1
    for i in range(m):
        li, ri = map(int, input().split())
        l = max(l, li)
        r = min(r, ri)
    print(max(r - l + 1, 0))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    l = [0] * (m + 1)
    r = [0] * (m + 1)
    for i in range(1, m + 1):
        l[i], r[i] = map(int, input().split())

    lmax = l[1]
    rmin = r[1]
    for i in range(2, m + 1):
        lmax = max(lmax, l[i])
        rmin = min(rmin, r[i])

    print(max(0, rmin - lmax + 1))

=======
Suggestion 6

def main():
    # input
    N, M = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(M)]

    # compute

    # output
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    l = 0
    r = N + 1
    for i in range(M):
        L, R = map(int, input().split())
        if l < L:
            l = L
        if r > R:
            r = R
    print(r - l + 1 if r >= l else 0)

=======
Suggestion 8

def solve():
    # Implement solution here
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    l = max(L)
    r = min(R)
    if r < l:
        print(0)
    else:
        print(r - l + 1)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)

    lmax = max(L)
    rmin = min(R)
    if lmax <= rmin:
        print(rmin-lmax+1)
    else:
        print(0)

=======
Suggestion 10

def read_ints():
  return list(map(int, input().split()))
