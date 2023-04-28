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
    print(max(0, min(R) - max(L) + 1))

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
    if L[M-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[M-1] + 1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()

    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L = max(L)
    R = min(R)
    if L <= R:
        print(R - L + 1)
    else:
        print(0)

=======
Suggestion 5

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
Suggestion 6

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0, min(R)-max(L)+1))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L = max(L)
    R = min(R)
    print(max(0, R - L + 1))

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
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
Suggestion 9

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    if l[m-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[m-1] + 1)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    ans = 0
    for i in range(1, n+1):
        if l[-1] <= i and i <= r[0]:
            ans += 1
    print(ans)
