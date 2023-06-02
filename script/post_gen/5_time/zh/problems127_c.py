Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l_max = max(l)
    r_min = min(r)
    if r_min < l_max:
        print(0)
    else:
        print(r_min - l_max + 1)

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
    print(min(R[0] - L[M - 1] + 1, N - M))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    l.sort()
    r.sort()
    if l[-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[-1] + 1)

=======
Suggestion 5

def problems127_c():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l1,r1 = map(int,input().split())
        l.append(l1)
        r.append(r1)
    print(max(0,min(r)-max(l)+1))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    L = [0] * m
    R = [0] * m
    for i in range(m):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    if L[m - 1] > R[0]:
        print(0)
    else:
        print(R[0] - L[m - 1] + 1)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()

    ans = 0
    for i in range(1, N + 1):
        l = 0
        r = 0
        while l < M and L[l] < i:
            l += 1
        while r < M and R[r] < i:
            r += 1
        ans += r - l
    print(ans)

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    max_l = max(L)
    min_r = min(R)
    if min_r < max_l:
        print(0)
    else:
        print(min_r - max_l + 1)
