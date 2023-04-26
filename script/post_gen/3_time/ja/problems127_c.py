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

    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

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
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 4

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
Suggestion 5

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l_max = max(l)
    r_min = min(r)
    if l_max <= r_min:
        print(r_min - l_max + 1)
    else:
        print(0)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    lmax = max(l)
    rmin = min(r)
    print(rmin-lmax+1 if rmin-lmax+1 > 0 else 0)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        li, ri = map(int, input().split())
        l = max(l, li)
        r = min(r, ri)
    print(max(r-l+1, 0))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l_max = max(l)
    r_min = min(r)
    if r_min-l_max+1 >= 0:
        print(r_min-l_max+1)
    else:
        print(0)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(m)]
    lrs.sort(key=lambda x: x[1])
    ans = 0
    r = 0
    for l, r in lrs:
        if r <= r:
            continue
        else:
            r = r
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    l = [0]*(n+1)
    r = [0]*(n+1)
    for i in range(m):
        a,b = map(int, input().split())
        l[a] += 1
        r[b] += 1
    ans = 0
    cnt = 0
    for i in range(1,n+1):
        cnt += l[i]
        if cnt == m:
            ans += 1
        cnt -= r[i]
    print(ans)
