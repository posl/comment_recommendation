Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    A = sorted(A, reverse=True)
    C = sorted(C, reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            i += 1
    print(sum(A))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(A))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m
    c = [0] * m
    for i in range(m):
        b[i], c[i] = map(int, input().split())
    a.sort()
    c.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            b[j] -= 1
            if b[j] == 0:
                j += 1
        i += 1
    print(sum(a))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        for k in range(BC[j][0]):
            if i >= N or A[i] >= BC[j][1]:
                break
            A[i] = BC[j][1]
            i += 1
    print(sum(A))
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(N):
        if i < M and BC[i][1] > A[i]:
            ans += BC[i][1]
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for j in range(b):
            if i < N and A[i] < c:
                A[i] = c
                i += 1
            else:
                break
    print(sum(A))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    c.sort(reverse=True)
    j = 0
    for i in range(n):
        if a[i] < c[j]:
            a[i] = c[j]
            j += 1
            if j == m:
                break
    print(sum(a))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    A.sort(reverse = True)
    BC.sort(key = lambda x: x[1], reverse = True)
    idx = 0
    for b, c in BC:
        for i in range(b):
            if idx >= N:
                break
            if A[idx] < c:
                A[idx] = c
                idx += 1
            else:
                break

    print(sum(A))

=======
Suggestion 9

def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(M)]

    # compute
    As.sort()
    BCs.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for B, C in BCs:
        for _ in range(B):
            if i >= N:
                break
            if As[i] >= C:
                break
            As[i] = C
            i += 1

    # output
    print(sum(As))

=======
Suggestion 10

def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs, Cs = [], []
    for _ in range(M):
        B, C = map(int, input().split())
        Bs.append(B)
        Cs.append(C)

    # compute
    As.sort(reverse=True)
    Cs.sort(reverse=True)
    for i in range(N):
        if i < M and As[i] < Cs[i]:
            As[i] = Cs[i]
        else:
            break

    # output
    print(sum(As))
