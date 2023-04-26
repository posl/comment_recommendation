Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(n):
        ok = n + 1
        ng = i
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if s[mid] - s[i] >= m:
                ok = mid
            else:
                ng = mid
        ans = max(ans, s[ok] - s[i] - m)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] % M)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * M
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(M):
        if B[i] == 0:
            ans = i
            break
    if ans == 0:
        ans = M
    print(ans)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = [0]*N
    for i in range(N):
        B[i] = A[i] % M
    C = [0]*M
    for i in range(N):
        C[B[i]] += 1
    C.sort()
    ans = 0
    for i in range(M):
        if C[i] == 0:
            continue
        else:
            ans += C[i]*i
            C[i+1] += C[i]
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * m
    for i in a:
        b[i] += 1
    c = 0
    for i in range(m):
        if b[i] == 0:
            c = i
            break
    d = 0
    for i in range(m):
        if b[i] > 1:
            d = i
            break
    if c == 0 and d == 0:
        print(0)
        return
    for i in range(m):
        if b[i] == 0:
            c = i
            break
    e = 0
    for i in range(m):
        if b[i] > 1:
            e = i
            break
    if c == 0 and e == 0:
        print(m)
        return
    f = 0
    for i in range(m):
        if b[i] >= 1:
            f += i
    if f == 0:
        print(m)
        return
    g = 0
    for i in range(m):
        if b[i] >= 1:
            g += i
    if g == 0:
        print(m)
        return
    h = 0
    for i in range(m):
        if b[i] >= 2:
            h += i
    if h == 0:
        print(m)
        return
    print(min(f,g,h))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > ans:
            ans += a[i] - ans
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(A[0] + M)
    D = []
    for i in range(N):
        D.append(A[i + 1] - A[i])
    D.sort(reverse=True)
    print(sum(D[N-1:]))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i%m for i in a]
    a.sort()
    a.append(a[0]+m)
    ans = 0
    for i in range(n):
        if a[i] > a[i+1]:
            ans += m - a[i] + a[i+1]
        else:
            ans += a[i+1] - a[i]
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] + a[i+1] if a[i] + a[i+1] < m else a[i] + a[i+1] - m
        if a[i] + a[i+1] >= m:
            a[i+1] = a[i] + a[i+1] - m
    print(ans)
