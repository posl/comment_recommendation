Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [tuple(map(int, input().split())) for _ in range(m)]

    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)

    i = 0
    for b, c in bc:
        for _ in range(b):
            if a[i] >= c:
                break
            a[i] = c
            i += 1
            if i == n:
                break
        if i == n:
            break
    print(sum(a))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while j < M:
        if i >= N:
            break
        if BC[j][1] <= A[i]:
            break
        else:
            for k in range(BC[j][0]):
                if i >= N:
                    break
                if BC[j][1] <= A[i]:
                    break
                A[i] = BC[j][1]
                i += 1
            j += 1
    print(sum(A))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b_i,c_i = map(int,input().split())
        b.append(b_i)
        c.append(c_i)
    b_c = list(zip(b,c))
    b_c.sort(key=lambda x:x[1],reverse=True)
    sum = 0
    for i in range(len(b_c)):
        for j in range(b_c[i][0]):
            if a[j] < b_c[i][1]:
                a[j] = b_c[i][1]
            else:
                break
    for i in range(n):
        sum += a[i]
    print(sum)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    A.sort()
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
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]

    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)

    i = 0
    for b, c in bc:
        for _ in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
                if i == n:
                    break
            else:
                break
        else:
            continue
        break

    print(sum(a))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if bc[j][0] > 0:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            i += 1
        else:
            j += 1
    print(sum(a))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)

    i = 0
    j = 0
    while i < n and j < m:
        b, c = bc[j]
        if a[i] < c:
            a[i] = c
            b -= 1
            if b == 0:
                j += 1
        else:
            i += 1

    print(sum(a))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for _ in range(m):
        bc.append(list(map(int, input().split())))
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if bc[j][0] == 0:
            j += 1
        else:
            a[i] = max(a[i], bc[j][1])
            bc[j][0] -= 1
            i += 1
    print(sum(a))

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = []
    c = []
    for i in range(m):
        b_,c_ = map(int, input().split())
        b.append(b_)
        c.append(c_)
    d = []
    for i in range(n):
        d.append(a[i])
    for i in range(m):
        for j in range(b[i]):
            if c[i] > d[-1]:
                d.pop()
            else:
                break
        for j in range(b[i]):
            d.append(c[i])
    print(sum(d))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        for k in range(BC[j][0]):
            if A[i+k] < BC[j][1]:
                A[i+k] = BC[j][1]
        i += BC[j][0]
    print(sum(A))
