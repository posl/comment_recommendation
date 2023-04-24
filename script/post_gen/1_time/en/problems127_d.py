Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N or A[i] >= c:
                break
            A[i] = c
            i += 1
    print(sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    bc.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for b, c in bc:
        for _ in range(b):
            if j < n and a[j] < c:
                a[j] = c
                j += 1
            else:
                break
        else:
            continue
        break
    print(sum(a))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            for _ in range(bc[j][0]):
                a[i] = bc[j][1]
                i += 1
                if i >= n:
                    break
            j += 1
        else:
            break
    print(sum(a))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b, c])
    bc.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for i in range(n):
        if j >= m:
            break
        if bc[j][1] > a[i]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        else:
            break
    print(sum(a))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1], reverse=True)

    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break

    print(sum(A))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(tuple(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if A[i] < c:
                A[i] = c
                i += 1
            else:
                break
            if i == N:
                break
        if i == N:
            break
    print(sum(A))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for i in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for j in range(b):
            if i < n and a[i] < c:
                a[i] = c
                i += 1
            else:
                break
    print(sum(a))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        x, y = map(int, input().split())
        b.append(x)
        c.append(y)
    d = []
    for i in range(n):
        d.append([a[i], 1])
    for i in range(m):
        d.append([c[i], b[i]])
    d.sort(reverse=True)
    ans = 0
    cnt = 0
    for i in range(n):
        ans += d[i][0]
    for i in range(n + m):
        if cnt >= n:
            break
        if d[i][1] == 1:
            continue
        for j in range(d[i][1]):
            ans += d[n + j][0] - d[cnt][0]
            cnt += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b, c])
    bc.sort(key=lambda x: x[1], reverse=True)

    i = 0
    for b, c in bc:
        for _ in range(b):
            if i < n and c > a[i]:
                a[i] = c
                i += 1
            else:
                break
        if i >= n:
            break

    print(sum(a))

=======
Suggestion 10

def solve(n, m, a, b, c):
    a.sort()
    for i in range(m):
        for j in range(b[i]):
            if a[j] < c[i]:
                a[j] = c[i]
            else:
                break
        a.sort()
    return sum(a)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
c = []
for i in range(m):
    bi, ci = map(int, input().split())
    b.append(bi)
    c.append(ci)
print(solve(n, m, a, b, c))
