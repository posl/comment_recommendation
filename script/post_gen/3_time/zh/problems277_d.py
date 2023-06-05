Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < m:
            ans += m - a[i]
        else:
            ans += a[i] % m
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    ans = 0
    for i in range(n):
        ans += a[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # A = [3, 0, 2, 5, 5, 3, 0, 6, 3]
    # M = 7
    # N = 9
    # A = [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]
    # M = 20
    # N = 20

    A.sort()

    if N == 1:
        print((M - A[0]) % M)
        return

    # print(A)

    ans = 0
    for i in range(N - 1):
        ans += (A[i + 1] - A[i] - 1) % M

    ans += (A[0] + M - A[N - 1] - 1) % M

    print(ans)

=======
Suggestion 4

def main():
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    n, m = 20, 20
    a = [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]
    a.sort()
    a.append(m)
    ans = 0
    i = 0
    while i < n:
        j = i
        while a[j] == a[j + 1]:
            j += 1
        ans += (a[j] - a[i]) // (m + 1)
        i = j + 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a[i] % m
    b.sort()
    c = [0] * n
    for i in range(n):
        c[i] = (b[i] + 1) % m
    c.sort()
    d = [0] * n
    for i in range(n):
        d[i] = (c[i] + 1) % m
    d.sort()
    e = [0] * n
    for i in range(n):
        e[i] = (d[i] + 1) % m
    e.sort()
    f = [0] * n
    for i in range(n):
        f[i] = (e[i] + 1) % m
    f.sort()
    g = [0] * n
    for i in range(n):
        g[i] = (f[i] + 1) % m
    g.sort()
    h = [0] * n
    for i in range(n):
        h[i] = (g[i] + 1) % m
    h.sort()
    i = [0] * n
    for i in range(n):
        i[i] = (h[i] + 1) % m
    i.sort()
    j = [0] * n
    for i in range(n):
        j[i] = (i[i] + 1) % m
    j.sort()
    k = [0] * n
    for i in range(n):
        k[i] = (j[i] + 1) % m
    k.sort()
    l = [0] * n
    for i in range(n):
        l[i] = (k[i] + 1) % m
    l.sort()
    m = [0] * n
    for i in range(n):
        m[i] = (l[i] + 1) % m
    m.sort()
    n = [0] * n
    for i in range(n):
        n[i] = (m[i] + 1) % m
    n.sort()
    o = [0] * n

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    for i in range(n):
        if i == 0:
            ans = a[i]
        else:
            ans += (a[i] - a[i-1] - 1)
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * m
    for i in a:
        b[i % m] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        ans += b[i]
        if i == m - i:
            b[i] = 0
        elif b[i] > b[m - i]:
            b[i] = b[m - i]
        else:
            b[m - i] = b[i]
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0] * (m+1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        if b[i+1] == 0:
            ans += i+1
            b[i+1] += 1
        b[i+1] -= 1
        b[i] -= 1
    print(ans)
main()

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if a[i] >= m:
            a[i] = a[i]%m
    res = 0
    for i in range(n):
        if a[i] != 0:
            res += a[i]
            if i != n-1:
                a[i+1] -= m-a[i]
    print(res)
solve()
