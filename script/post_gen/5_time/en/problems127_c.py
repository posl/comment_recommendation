Synthesizing 10/10 solutions (Duplicates hidden)

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
    L = max(L)
    R = min(R)
    if L <= R:
        print(R - L + 1)
    else:
        print(0)

=======
Suggestion 2

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
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0]-L[-1]+1)

=======
Suggestion 3

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
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L_max = max(L)
    R_min = min(R)
    if R_min < L_max:
        print(0)
    else:
        print(R_min - L_max + 1)

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    print(max(0, min(r) - max(l) + 1))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        li, ri = map(int, input().split())
        l = max(l, li)
        r = min(r, ri)
    print(max(0, r-l+1))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        l_i, r_i = map(int, input().split())
        if l_i > l:
            l = l_i
        if r_i < r:
            r = r_i
    if r >= l:
        print(r - l + 1)
    else:
        print(0)

=======
Suggestion 8

def solve():
    n,m = map(int,input().split())
    l = 0
    r = n
    for _ in range(m):
        x,y = map(int,input().split())
        l = max(l,x)
        r = min(r,y)
    print(max(r-l+1, 0))
solve()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    LRs = [tuple(map(int, input().split())) for _ in range(M)]

    LRs.sort(key=lambda x: x[0])
    maxR = LRs[0][1]
    ans = 1
    for L, R in LRs[1:]:
        if L > maxR:
            ans += 1
            maxR = R
        else:
            maxR = max(maxR, R)
    print(ans)
