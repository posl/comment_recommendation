Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    L = []
    R = []
    for i in range(m):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[m-1] > R[0]:
        print(0)
    else:
        print(R[0]-L[m-1]+1)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
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
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        ll, rr = map(int, input().split())
        l = max(l, ll)
        r = min(r, rr)
    print(max(0, r - l + 1))

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
    if r_min - l_max >= 0:
        print(r_min - l_max + 1)
    else:
        print(0)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    lmax = max(l)
    rmin = min(r)
    print(max(0, rmin - lmax + 1))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    print(min(r) - max(l) + 1 if min(r) - max(l) >= 0 else 0)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    print(max(0, min(r) - max(l) + 1))

=======
Suggestion 10

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
    print(max(r_min - l_max + 1, 0))
